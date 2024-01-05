from src import loading as load

from src.settings import main_dir, image_dir, sound_dir


all_scores = load.load_all_scores()


pattern_timings = [
    [500, 500, 250, 250, 500, 750, 250],
    [500, 250, 250, 250, 1250, 500],
    [1750, 250, 500, 250, 250],
    [1500, 1000, 500],
    [250, 750, 250, 1000, 250, 250, 250],
    [250, 250, 750, 250, 500, 250],

    [250, 500, 250, 250, 750, 250, 500, 250],
    [250, 250, 250, 500, 750, 500, 250],
    [500, 500, 250, 250, 750, 500],
    [500, 500, 250, 500],
    [250, 250, 750, 1250],
    [250, 250, 500, 750, 250, 250, 250, 500],
    [250, 250, 500, 750, 500, 250, 500],
    [500, 1000, 750, 250],
    [500, 750, 500, 250, 250, 250, 250]
]

patterns = [{'timings': u, 'score': v} for u,v in zip(pattern_timings, all_scores)]




'''
[500, 500, 250, 250, 500, 750, 250],
[500, 250, 250, 250, 1250, 500],
[1750, 250, 500, 250, 250],
[1500, 1000, 500],
[250, 750, 250, 1000, 250, 250, 250],
[250, 250, 750, 250, 500, 250]
'''


'''
[250, 500, 250, 250, 750, 250, 500, 250],
[0, 250, 250, 500, 750, 500, 250],
[250, 250, 250, 500, 750, 500, 250],
[500, 500, 250, 250, 750, 500],
[500, 500, 250, 500],
[250, 250, 666.6666666666666, 1250],
[0, 250, 750, 1250],
[250, 250, 750, 1250],
[250, 250, 500, 750, 250, 250, 250, 500],
[250, 250, 500, 750, 500, 250, 500],
[333.3333333333333, 1000, 750, 250],
[0, 1000, 750, 250],
[500, 1000, 750, 250],
[500, 750, 500, 250, 250, 250, 250]
'''







