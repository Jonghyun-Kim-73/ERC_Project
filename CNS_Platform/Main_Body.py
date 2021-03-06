import argparse
from multiprocessing.managers import BaseManager
from multiprocessing import Process
from collections import deque

from db import db_make

# from CNS_Run_Freeze import RUN_FREEZE
from CNS_Platform_controller import InterfaceFun
from CNS_All_module import All_Function_module
# import CNS_Platform_PARA as PARA


class Body:
    def __init__(self):
        # from AUTO_UI_TO_PY import AutoUiToPy
        # AutoUiToPy._ui_to_py()

        # 초기 입력 인자 전달 --------------------------------------------------------------------------------------------
        parser = argparse.ArgumentParser(description='CNS 플랫폼_Ver0')
        parser.add_argument('--comip', type=str, default='', required=False, help="현재 컴퓨터의 ip [default='']")
        parser.add_argument('--comport', type=int, default=7101, required=False, help="현재 컴퓨터의 port [default=7001]")
        parser.add_argument('--cnsip', type=str, default='192.168.0.101', required=False, help="CNS 컴퓨터의 ip [default='']")
        parser.add_argument('--cnsport', type=int, default=7101, required=False, help="CNS 컴퓨터의 port [default=7001]")
        self.args = parser.parse_args()
        print('=' * 25 + '초기입력 파라메터' + '=' * 25)

    def start(self):
        # 공유 메모리 선언 -----------------------------------------------------------------------------------------------
        BaseManager.register('SHMem', SHMem)
        manager = BaseManager()
        manager.start()

        shmem = manager.SHMem(cnsinfo=(self.args.cnsip, self.args.cnsport),
                              max_len_deque=20,
                              )
        # Build Process ------------------------------------------------------------------------------------------------
        p_list = []
        # Build AI-CNS
        p = InterfaceFun(shmem)
        p_list.append(p)

        # Build Interface
        p = All_Function_module(shmem)
        p_list.append(p)

        # --------------------------------------------------------------------------------------------------------------
        [p_.start() for p_ in p_list]
        [p_.join() for p_ in p_list]  # finished at the same time
        # End ----------------------------------------------------------------------------------------------------------


class SHMem:
    def __init__(self, cnsinfo, max_len_deque):
        self.cnsip, self.cnsport = cnsinfo
        # 0] 기능 동작 로직
        self.SV = True
        self.RC = False      # Rod Controller
        self.EC = True      # Emergency Controller
        self.ABD = True     # Abnormal Diagnosis

        # 1] CNS 변수용 shmem
        self.mem = db_make().make_mem_structure(max_len_deque)
        print('Main 메모리 생성 완료')
        # 2] Trig 변수용 shmem
        self.logic = {'Run': False, 'UpdateUI': False,
                      'Run_sv': self.SV, 'Run_rc': self.RC, 'Run_ec': self.EC,
                      'Run_abd': self.ABD,

                      'Initial_condition': False,
                      'Init_Call': False, 'Init_nub': 1,

                      'Mal_Call': False, 'Mal_list': {},

                      'Speed_Call': False, 'Speed': 1,
                      'Auto_Call': False, 'Auto_re_man': False,

                      'Rod_Control_Call': True,

                      'Operation_Strategy': 'N',  # Normal, Abnormal, Em
                      'Operation_Strategy_list': deque(maxlen=2),

                      'AB_DIG': [], 'Find_AB_DIG': False,
                      'SV_RES': [],

                      'LCO_Dict': {},
                      }
        print('Trig 메모리 생성 완료')
        # 3] 변수 그래픽 표기용
        self.save_mem = {
            'KCNTOMS': [],      'UAVLEG2': [],      'ZINST65': [],
            'cCOOLRATE': [],

            'BPRZSP': [], 'QPRZH': [], 'KLAMPO118': [],
            'BHV22': [], 'KLAMPO70': [],

            'KLAMPO134': [], 'KLAMPO135': [], 'KLAMPO136': [],
            'WAFWS1': [], 'WAFWS2': [], 'WAFWS3': [],
            'PMSS': [], 'BHTBY': [],

            'UP_D': [], 'DOWN_D': [], 'QPROREL': [], 'UAVLEGS': [], 'UAVLEGM': [], 'KBCDO20': [], 'KBCDO21': [],
            'KBCDO22': [], 'KBCDO16': [], 'BOR': [], 'MAKE_UP': [],
        }

    def call_init(self, init_nub):
        self.logic = {'Run': False, 'UpdateUI': False,
                      'Run_sv': self.SV, 'Run_rc': self.RC, 'Run_ec': self.EC,
                      'Run_abd': self.ABD,

                      'Initial_condition': True,
                      'Init_Call': True, 'Init_nub': init_nub,

                      'Mal_Call': False, 'Mal_list': {},

                      'Speed_Call': False, 'Speed': 1,
                      'Auto_Call': False, 'Auto_re_man': False,

                      'Rod_Control_Call': False,

                      'Operation_Strategy': 'N',  # Normal, Abnormal, Em
                      'Operation_Strategy_list': deque(maxlen=2),

                      'AB_DIG': [], 'Find_AB_DIG': False,
                      'SV_RES': [],

                      'LCO_Dict': {},
                      }

        for key in self.save_mem:
            self.save_mem[key].clear()

    def append_strategy_list(self, st):
        self.logic['Operation_Strategy_list'].append(st)

    def append_lco_dict(self, lco_name, Start_time, End_time):
        self.logic['LCO_Dict'][lco_name] = {'St': Start_time, 'Et': End_time}

    def change_mal_val(self, mal_index, mal_dict):
        self.logic['Mal_list'][mal_index] = mal_dict
        self.logic['Mal_Call'] = True

    def change_logic_val(self, key, val):
        self.logic[key] = val

    def change_mal_list(self, nub):
        self.logic['Mal_list'][nub]['Mal_done'] = True

    def change_shmem_db(self, mem):
        saved_mem_key = self.save_mem.keys()

        for key_val in mem.keys():
            self.mem[key_val] = mem[key_val]
            if key_val in saved_mem_key:
                self.save_mem[key_val].append(mem[key_val]['Val'])

    def get_speed(self, speed):
        self.logic['Speed_Call'] = True
        self.logic['Speed'] = speed
        return str(speed)

    def get_logic(self, key):
        return self.logic[key]

    def get_logic_info(self):
        return self.logic

    def get_cns_info(self):
        return self.cnsip, self.cnsport

    def get_shmem_val(self, val_name):
        return self.mem[val_name]['Val']

    def get_shmem_vallist(self, val_name):
        return self.mem[val_name]['List']

    def get_shmem_malinfo(self):
        return self.logic['Mal_Call'], self.logic['Mal_list']

    def get_shmem_db(self):
        return self.mem

    def get_shmem_save_db(self):
        return self.save_mem


if __name__ == '__main__':
    main_process = Body()
    main_process.start()
