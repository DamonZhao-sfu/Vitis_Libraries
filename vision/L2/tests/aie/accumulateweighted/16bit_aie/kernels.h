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

#ifndef _KERNELS_H_
#define _KERNELS_H_

#include <adf/stream/types.h>
#include <adf/io_buffer/io_buffer.h>
#include <stdint.h>
#include <stdlib.h>

void accumulateweighted(adf::input_buffer<int16>& input1,
                        adf::input_buffer<int16>& input2,
                        adf::output_buffer<int16>& output,
                        float alpha);

#endif
