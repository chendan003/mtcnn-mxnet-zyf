# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 02:22:54 2017

@author: zhaoy
"""
from __future__ import print_function
import os
import os.path as osp

import time
import cv2

import _init_paths
from face_aligner import FaceAligner


if __name__ == '__main__':
    show_img = True

    model_path = '../../model'
    save_dir = './face_chips'
    #    save_json = 'mtcnn_align_test_rlt.json'

    if not osp.exists(save_dir):
        os.makedirs(save_dir)

    img_path = '../../test_imgs/Marilyn_Monroe_0002.jpg'
    face_rect1 = [
        [
            91,
            57
        ],
        [
            173,
            57
        ],
        [
            173,
            180
        ],
        [
            91,
            180
        ]
    ]

    face_rects = [face_rect1]

    base_name = osp.basename(img_path)
    name, ext = osp.splitext(base_name)
    ext = '.png'

    #    fp_rlt = open(osp.join(save_dir, save_json), 'w')
    #    results = []

    img = cv2.imread(img_path)

    aligner = FaceAligner(model_path)

    t1 = time.clock()
    # You can align the faces in two steps like this:
    #    bboxes, points = aligner.align_face(img, face_rects)
    #    face_chips = aligner.get_face_chips(img, bboxes, points)

    # OR just align them in one step by calling the following function,
    # which combine last two functions
    face_chips = aligner.get_face_chips(img, face_rects)
    t2 = time.clock()

    for i, chip in enumerate(face_chips):
        print('---> chip.shape: ', chip.shape)
        save_name = osp.join(save_dir, 'face_chip_%s_%d' % (name, i) + ext)
        cv2.imwrite(save_name, chip)

        if show_img:
            cv2.imshow('face_chip', chip)

            cv2.waitKey(0)

    n_boxes = len(face_rects)
    print("-->Alignment cost %f seconds, processed %d face rects, avg time: %f seconds" %
          ((t2 - t1), n_boxes, (t2 - t1) / n_boxes))

    #    rlt = {}
    #    rlt["filename"] = img_path
    #    rlt["faces"] = []
    #    rlt['face_count'] = 0
    #
    #    if bboxes is not None and len(bboxes) > 0:
    #        for (box, pts) in zip(bboxes, points):
    #            #                box = box.tolist()
    #            #                pts = pts.tolist()
    #            tmp = {'rect': box[0:4],
    #                   'score': box[4],
    #                   'pts': pts
    #                   }
    #            rlt['faces'].append(tmp)
    #
    #    rlt['face_count'] = len(bboxes)
    #
    #    rlt['message'] = 'success'
    #    results.append(rlt)
    #
    #    json.dump(results, fp_rlt, indent=4)
    #    fp_rlt.close()

    #    draw_faces(img, bboxes, points)
    #
    #    save_name = osp.join(save_dir, name + ext)
    #    cv2.imwrite(save_name, img)
    #
    #    if show_img:
    #        cv2.imshow('img', img)
    #
    #        cv2.waitKey(0)
    #
    if show_img:
        cv2.destroyAllWindows()
