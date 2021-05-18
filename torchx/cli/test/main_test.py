#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import unittest
from pathlib import Path

import torchelastic.tsm.driver as tsm
from torchx.cli.cmd_run import _parse_run_config
from torchx.cli.main import main

_root: Path = Path(__file__).parent


class CLITest(unittest.TestCase):
    def test_run(self) -> None:
        main(
            [
                "run",
                "--scheduler",
                "local",
                str(_root / "examples" / "simple.conf"),
                "--num_trainers",
                "2",
                "--trainer_image",
                str(_root / "examples" / "container"),
            ]
        )

    def test_run_scheduler_args_empty(self) -> None:
        self.assertEqual(_parse_run_config(""), tsm.RunConfig())

    def test_run_scheduler_args_simple(self) -> None:
        self.assertEqual(
            _parse_run_config("a=1,b=2;3;4"),
            tsm.RunConfig(
                cfgs={
                    "a": "1",
                    "b": ["2", "3", "4"],
                }
            ),
        )
