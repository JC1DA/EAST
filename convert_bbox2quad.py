from glob import glob
import os

ICDAR_BBBOXGT_DIR = './data/icdar2013_gt'
QUADGT_DIR = './data/icdar2013'

gt_paths = glob(ICDAR_BBBOXGT_DIR + '/*.txt')
for gt_path in gt_paths:
    lines = tuple(open(gt_path))

    #remove gt_ in output name
    gt_out_name = os.path.basename(gt_path).replace('gt_', '')
    f = open(os.path.join(QUADGT_DIR, gt_out_name), 'w')
    for line in lines:
        data = line.split(' ')
        left = int(data[0])
        top  = int(data[1])
        right = int(data[2])
        bot   = int(data[3])
        gt = data[4].replace('\n','')

        f.write('{},{},{},{},{},{},{},{},{}\n'.format(
            left, top,
            right, top,
            right, bot,
            left, bot,
            gt))
    f.close()