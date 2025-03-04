/*
 * Copyright (C) 2019-2022, Xilinx, Inc.
 * Copyright (C) 2022-2023, Advanced Micro Devices, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef _XF_IMG_PYRAMID_PARAMS_H_
#define _XF_IMG_PYRAMID_PARAMS_H_

// NPC parameter
#define NPC_PYRAMID XF_NPPC1

// port widths
#define IMAGE_PTR_WIDTH_P 128

// Internal Parameter
#define IMG_BW_P 8
#define IMG_TYPE_P XF_8UC1
#define IMG_F_BITS_P 0
#define MAX_NUM_LEVELS_P 16

///////Debug macros
#define DEBUG_P 0

// Resize Macros
#define MAXDOWNSCALE_P 2
#define INTERPOLATION_P 1
#define NEWWIDTH 512
#define NEWHEIGHT 512
#define WIDTH 512
#define HEIGHT 512
#define XF_USE_URAM 1
#define XF_CV_DEPTH_in_mat 2
#define XF_CV_DEPTH_out_mat 2

#endif // _XF_IMG_PYRAMID_PARAMS_H_
