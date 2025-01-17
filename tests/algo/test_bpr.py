# -*- coding: utf-8 -*-
import unittest

import numpy as np

from buffalo.misc import aux
from buffalo.algo.bpr import BPRMF
from buffalo.misc.log import set_log_level
from buffalo.algo.options import BPRMFOption

from .base import TestBase


class TestBPRMF(TestBase):
    def test0_get_default_option(self):
        BPRMFOption().get_default_option()
        self.assertTrue(True)

    def test1_is_valid_option(self):
        opt = BPRMFOption().get_default_option()
        self.assertTrue(BPRMFOption().is_valid_option(opt))
        opt['save_best'] = 1
        self.assertRaises(RuntimeError, BPRMFOption().is_valid_option, opt)
        opt['save_best'] = False
        self.assertTrue(BPRMFOption().is_valid_option(opt))

    def test2_init_with_dict(self):
        set_log_level(3)
        opt = BPRMFOption().get_default_option()
        BPRMF(opt)
        self.assertTrue(True)

    def test3_init(self):
        opt = BPRMFOption().get_default_option()
        self._test3_init(BPRMF, opt)

    def test4_train(self):
        opt = BPRMFOption().get_default_option()
        opt.d = 5
        self._test4_train(BPRMF, opt)

    def test5_validation(self):
        np.random.seed(7)
        opt = BPRMFOption().get_default_option()
        opt.d = 5
        opt.num_workers = 4
        opt.num_iters = 500
        opt.random_seed = 7
        opt.validation = aux.Option({'topk': 10})
        opt.tensorboard = aux.Option({'root': './tb',
                                      'name': 'bpr'})

        self._test5_validation(BPRMF, opt, ndcg=0.03, map=0.02)

    def test6_topk(self):
        opt = BPRMFOption().get_default_option()
        opt.d = 5
        opt.num_iters = 200
        opt.validation = aux.Option({'topk': 10})
        self._test6_topk(BPRMF, opt)

    def test7_train_ml_20m(self):
        opt = BPRMFOption().get_default_option()
        opt.num_workers = 8
        opt.validation = aux.Option({'topk': 10})
        self._test7_train_ml_20m(BPRMF, opt)

    def test8_serialization(self):
        opt = BPRMFOption().get_default_option()
        opt.num_iters = 200
        opt.d = 5
        opt.validation = aux.Option({'topk': 10})

        self._test8_serialization(BPRMF, opt)

    def test9_compact_serialization(self):
        opt = BPRMFOption().get_default_option()
        opt.num_iters = 200
        opt.d = 5
        opt.validation = aux.Option({'topk': 10})
        self._test9_compact_serialization(BPRMF, opt)

    def test10_fast_most_similar(self):
        opt = BPRMFOption().get_default_option()
        opt.d = 5
        opt.validation = aux.Option({'topk': 10})
        self._test10_fast_most_similar(BPRMF, opt)

if __name__ == '__main__':
    unittest.main()
