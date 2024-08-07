import os 
import unittest

import bruce


class TestCase(unittest.TestCase):
    def test_types(self):
        self.assertTrue('ACTUAL' in dir(bruce))


    def test_stimulus(self):
        stim = bruce.stimulus.ramped_sine_wave(.25, .3, int(100e3), 2.5e-3, 25e-3, int(5e3), 60.0)
        self.assertAlmostEqual(stim.stimulus_duration, 0.275)
        self.assertEqual(stim.sampling_rate, int(100e3))

    def test_read_stimulus(self):
        root = os.path.dirname(os.path.dirname(__file__))
        stim = bruce.stimulus.from_file(os.path.join(root, "data/defineit.wav"), False)
        self.assertAlmostEqual(stim.stimulus_duration, 0.891190)
        self.assertEqual(stim.sampling_rate, int(100e3))

    def test_neurogram(self):
        stim = bruce.stimulus.ramped_sine_wave(.1, .3, int(100e3), 2.5e-3, 25e-3, int(5e3), 60.0)
        ng = bruce.Neurogram(2)
        ng.bin_width = stim.time_resolution

        ng.create(stim, 1)

        binned_output = ng.get_output()
        self.assertEqual(binned_output.shape[0], 2)
        self.assertEqual(binned_output.shape[1], int(stim.n_simulation_timesteps / (ng.bin_width / stim.time_resolution)))
    

if __name__ == "__main__":
    unittest.main()