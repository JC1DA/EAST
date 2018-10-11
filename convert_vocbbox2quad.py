from glob import glob
import os
import untangle

BBBOXGT_DIR = './data/cbsn_news_gt'
QUADGT_DIR = './data/cbsn_news'

gt_paths = glob(BBBOXGT_DIR + '/*.xml')

for gt_path in gt_paths:
    gt_out_name = os.path.basename(gt_path).replace('xml','txt')

    gt_obj = untangle.parse(gt_path).annotation

    f = open(os.path.join(QUADGT_DIR, gt_out_name), 'w')
    for gt in gt_obj.object:
        bbox = gt.bndbox
        gt_text = gt.name.cdata

        left = bbox.xmin.cdata
        right = bbox.xmax.cdata
        top = bbox.ymin.cdata
        bot = bbox.ymax.cdata

        f.write('{},{},{},{},{},{},{},{},{}\n'.format(
            left, top,
            right, top,
            right, bot,
            left, bot,
            gt_text))

    f.close()
