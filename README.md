# Digital Image Processing Techniques
**Note:** This repository contains various digital image processing techniques implemented in Python3 & OpenCV.

### 1. Image Augmentation and Shearing
- [Image Augmentation Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_1/src/image_translation.py)
- [Image Shearing Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_1/src/image_shear.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_1/results)
```sh
python src/method_1/src/image_shear.py
python src/method_1/src/image_translation.py
```

<p float="left">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_1/results/image_aug_1.PNG" height="80" />
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_1/results/image_aug_1.PNG" height="80" />
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_1/results/image_aug_1.PNG" height="80" />
</p>

### 2. Intensity Transformation
- [Intensity Transformation: Negative, Gamma-mode, Log-mode, Normalization Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_2/src/intensity_transformation.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_2/results)
```sh
python src/method_2/src/intensity_transformation.py
```

### 3. Local Histogram Equivalent
- [Local Histogram Equivalent Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_3/src/local_histogram_equal.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_3/results)
```sh
python src/method_3/src/local_histogram_equal.py
```

### 4. Spatial Filter
- [Lowpass Filter Gaussian Blur Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_4/src/low_pass_filter_a/lpf_gaussian.py)
- [Lowpass Filter Gaussian Blur with Threshold Code](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_4/src/low_pass_filter_b/lpf_gaussian.py)
- [Lowpass Filter Gaussian Blur & Normalization Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_4/src/low_pass_filter_c/lpf_gaussian.py)
- [Unsharp Masking Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_4/src/unsharp_masking/unsharp_masking.py)
- [High Boost Filtering Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_4/src/high_boost_filter/high_boost_filter.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_4/results)
```sh
python src/method_4/src/low_pass_filter_a/lpf_gaussian.py
python src/method_4/src/low_pass_filter_b/lpf_gaussian.py
python src/method_4/src/low_pass_filter_c/lpf_gaussian.py
python src/method_4/src/unsharp_masking/unsharp_masking.py
python src/method_4/src/high_boost_filter/high_boost_filter.py
```

### 5. Filter in Frequency Domain
- [Gaussian Lowpass Filter in Frequency Domain Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_5/src/gaussian_lpf_freq/gaussian_lpf_freq.py)
- [Butterworth Lowpass Filter in Frequency Domain Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_5/src/bufferworth_lpf_freq/bufferworth_lpf_freq.py)
- [Gaussian Lowpass Filter & Normalization in Frequency Domain Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_5/src/gaussian_lpf_norm_freq/gaussian_lpf_norm_freq.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_5/results)
```sh
python src/method_5/src/gaussian_lpf_freq/gaussian_lpf_freq.py
python src/method_5/src/bufferworth_lpf_freq/bufferworth_lpf_freq.py
python src/method_5/src/gaussian_lpf_norm_freq/gaussian_lpf_norm_freq.py
```

### 6. Adaptive Median Filter
- [Adaptive Median Filter Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_6/src/amf.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_6/results)
```sh
python src/method_6/src/amf.py
```

### 7. Frequency Domain Filter for Motion Deblurring
- [Frequency Domain Filter for Motion Deblurring - Pseudo Filter vs Wiener Filter Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_7/src/deblur.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_7/results)
```sh
python src/method_7/src/deblur.py
```

### 8. Canny Edge Detection
- [Canny Edge Detection Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_8/src/canny_edge_detection.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_8/results)
```sh
python src/method_8/src/canny_edge_detection.py
```

### 9. Gaussian Pyramid & Laplacian Pyramid Filter
- [Gaussian and Laplacian Pyramid Filter Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_9/src/gauss_laplace_pyramid.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_9/results)
```sh
python src/method_9/src/gauss_laplace_pyramid.py
```

### 10. Gaussian & Laplacian Pyramid Blend
- [Gaussian & Laplacian Pyramid Blend Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_10/src/gauss_laplace_pyramid_blend.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_10/results)
```sh
python src/method_10/src/gauss_laplace_pyramid_blend.py
```

### 11. Ideal & Gaussian Bandpass Filters
- [Ideal Bandpass Filter Code](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_11/src/ideal_bandpass_filter)
- [Gaussian Bandpass Filter Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_11/src/gaussian_bandpass_filter/gaussian_bandpass_filter.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_11/results)
```sh
python src/method_11/src/gaussian_bandpass_filter/gaussian_bandpass_filter.py
python src/method_11/src/ideal_bandpass_filter/ideal_bandpass_filter.py
```



