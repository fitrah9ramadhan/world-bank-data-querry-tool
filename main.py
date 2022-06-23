from worldbank import WorldBankDataTransform, Visualization

import constant as c
import helper


def main():
    filename = helper.get_filename_dict(c.DATA_PATH)
    wb_files = WorldBankDataTransform(filename=filename)

    wb_files.multivar_panel_data(save_file=True, filename_save='rich_panel_data.csv')

if __name__ == '__main__':
    main()



