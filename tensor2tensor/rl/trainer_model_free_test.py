# coding=utf-8
# Copyright 2019 The Tensor2Tensor Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests of basic flow of collecting trajectories and training PPO."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensor2tensor.rl import trainer_model_free
from tensor2tensor.utils import registry

import tensorflow as tf

FLAGS = tf.flags.FLAGS


class TrainTest(tf.test.TestCase):

  def test_train_pong(self):
    hparams = registry.hparams("rlmf_original")
    hparams.batch_size = 2
    hparams.eval_sampling_temps = [0.0, 1.0]
    hparams.add_hparam("ppo_epochs_num", 2)
    hparams.add_hparam("ppo_epoch_length", 3)
    FLAGS.output_dir = tf.test.get_temp_dir()
    trainer_model_free.train(hparams, FLAGS.output_dir)


if __name__ == "__main__":
  tf.test.main()
