from pygame import display
from options import resolutions


def load_save_data(save_file):
    try:
        # save info.txt has all saved settings
        save_info = open(save_file, 'r')
        for line in save_info:
            if line[0] == 'I':
                input_method = ''
                for num in range(len(line)-3):
                    input_method += line[num+2]
            if line[0] == 'C':
                chosen_class = ''
                for num in range(len(line)-3):
                    chosen_class += line[num+2]
            if line[0] == 'M':
                mode = ''
                for num in range(len(line)-3):
                    mode += line[num+2]
            if line[0] == 'H':
                high_score = ''
                for num in range(len(line)-3):
                    high_score += line[num+2]
            if line[0] == 'R':
                resolution = ''
                for num in range(len(line)-3):
                    resolution += line[num+2]
        # the info list is to make sure that all needed data is found
        info = [input_method, chosen_class, mode, high_score, resolution]
    except:
        print('save data is corrupted')
        input_method = 'keyboard' # can be in 'keyboard' or 'mouse' mode
        chosen_class = 'ranger' # can be 'ranger' or 'knight' with 'ranger' being default
        mode = 'castle' # 'dungeon', 'crypt', and 'castle' are normal mode and 'endless' is the wave based mode
        high_score = 0 # zero is the base high score
        # take the list of resolutions from before and turn them into integers
        res = []
        for resolution in resolutions: res.append(int(resolution))
        best_res = min(res, key=lambda x: abs(x - display.Info().current_h)) 
        resolution = best_res # makes the screen resolution the closest availible resolution

    return input_method, chosen_class, mode, high_score, int(resolution)


def write_save_data(save_file, input_method, chosen_class, mode, high_score, resolution):
    save_info = open(save_file, 'w')
    save_info.write(f'I {input_method}\n')
    save_info.write(f'C {chosen_class}\n')
    save_info.write(f'M {mode}\n')
    save_info.write(f'H {high_score}\n')
    save_info.write(f'R {resolution}\n')