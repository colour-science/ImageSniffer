import unittest

from pathlib import Path

from characterization_sequence import CharacterizationSequence

CROPPED_HOT_SEQUENCE_DIR_PATH = '/Users/jgoldstone/Content/not_secret_content/arri/bur/tfe/aces/vwg_gm/balloon+2XL5-C_demo_mode_test/derived/seqs/A003R3VC/A003C003_120101_cropped'
CROPPED_
# start at 1, end at 7212
TEST_FIRST_FRAME = 1000
TEST_LAST_FRAME = 1050

class C18nSequenceTestCase(unittest.TestCase):

    def test_sequence_loads(self):
        frame_paths_to_test = ['/tmp/foo.01.exr', '/tmp/foo.00.exr', '/tmp/foo.02.exr']
        for frame_path in frame_paths_to_test:
            open(frame_path, 'a').close()
        c18n = CharacterizationSequence('/tmp', 'foo', 2, 0, 2)
        expected = sorted(frame_paths_to_test)
        actual = [str(fp) for fp in sorted(c18n.frame_paths)]
        self.assertEqual(expected, actual)

    # def test_real_sequence_subset_loads(self):
    #     dir_path = '/Users/jgoldstone/Content/not_secret_content/arri/bur/tfe/aces/vwg_gm/balloon+2XL5' \
    #                '-C_demo_mode_test/derived/seqs/A003R3VC/A003C003_120101_cropped'
    #     # dir_path = '/tmp'
    #     file_base = 'A003C003_120101_cropped'
    #     # file_base = 'green_negative_sprinkle_at_x0174_y_0980'
    #     frame_number_width = 4
    #     # frame_number_width = 0
    #     first = 1
    #     last = 7212
    #     c18n = CharacterizationSequence(dir_path, file_base, frame_number_width, first, last)
    #     # c18n = CharacterizationSequence(dir_path, file_base, 0, 0, 0)
    #     # self.assertEqual(1 + last - first, len(c18n.frame_paths))
    #     c18n.characterize_frames()
    #     print(str(c18n))


if __name__ == '__main__':
    unittest.main()
