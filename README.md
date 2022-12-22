# Digital Image Processing Techniques
**Note:** This repository contains various digital image processing techniques implemented in Python3 & OpenCV.

## 1. Image Augmentation and Shearing
<p float="left">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_1/results/image_aug_1.PNG" height="100" />
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_1/results/image_aug_2.PNG" height="100" />
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_1/results/image_shear_1.PNG" height="100" />
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_1/results/image_shear_2.PNG" height="100" />
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_1/results/image_shear_3.PNG" height="100" />
</p>
- [Image Augmentation Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_1/src/image_translation.py)
- [Image Shearing Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_1/src/image_shear.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_1/results)
```sh
python src/method_1/src/image_shear.py
python src/method_1/src/image_translation.py
```

## 2. Intensity Transformation
<p float="left">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_2/results/spillway_gamma_mode.PNG" width="100">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_2/results/spillway_log_mode.PNG" width="100">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_2/results/spillway_negative_mode.PNG" width="100">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_2/results/spillway_normalized_unormalized_gamma_mode.PNG" width="100">
</p>
- [Intensity Transformation: Negative, Gamma-mode, Log-mode, Normalization Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_2/src/intensity_transformation.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_2/results)
```sh
python src/method_2/src/intensity_transformation.py
```

## 3. Local Histogram Equivalent
<p float="left">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_3/results/symbol_review.PNG" width="100">
</p>
- [Local Histogram Equivalent Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_3/src/local_histogram_equal.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_3/results)
```sh
python src/method_3/src/local_histogram_equal.py
```

## 4. Spatial Filter
<p float="left">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_4/results/lpf_gaussian_a.PNG" width="100">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_4/results/lpf_gaussian_b.PNG" width="100">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_4/results/lpf_gaussian_c.PNG" width="100">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_4/results/high_boost_filter.PNG" width="100">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_4/results/unsharp_masking.PNG" width="100">
</p>
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

## 5. Filter in Frequency Domain
<p float="left">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_5/results/gaussian_lpf_freq.PNG" width="100">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_5/results/butterworth_lpf_freq.PNG" width="100">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_5/results/gaussian_lpf_norm_freq.PNG" width="100">
</p>
- [Gaussian Lowpass Filter in Frequency Domain Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_5/src/gaussian_lpf_freq/gaussian_lpf_freq.py)
- [Butterworth Lowpass Filter in Frequency Domain Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_5/src/bufferworth_lpf_freq/bufferworth_lpf_freq.py)
- [Gaussian Lowpass Filter & Normalization in Frequency Domain Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_5/src/gaussian_lpf_norm_freq/gaussian_lpf_norm_freq.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_5/results)
```sh
python src/method_5/src/gaussian_lpf_freq/gaussian_lpf_freq.py
python src/method_5/src/bufferworth_lpf_freq/bufferworth_lpf_freq.py
python src/method_5/src/gaussian_lpf_norm_freq/gaussian_lpf_norm_freq.py
```

## 6. Adaptive Median Filter
<p float="left">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_6/results/amf_vs_built_in_filter.PNG" width="100">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_6/results/gauss_noised_corrupted.PNG" width="100">
</p>
- [Adaptive Median Filter Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_6/src/amf.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_6/results)
```sh
python src/method_6/src/amf.py
```

## 7. Frequency Domain Filter for Motion Deblurring
<p float="left">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_7/results/pseudo_vs_wiener_filter.PNG" width="100">
</p>
- [Frequency Domain Filter for Motion Deblurring - Pseudo Filter vs Wiener Filter Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_7/src/deblur.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_7/results)
```sh
python src/method_7/src/deblur.py
```

## 8. Canny Edge Detection
<img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_8/results/blended_canny_detection.PNG" width="100">
<img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_8/results/canny_edge_different_levels.PNG" width="100">
<img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_8/results/gauss_blur_different_levels.PNG" width="100">
<img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_8/results/gradient_mag_and_angle.PNG" width="100">
<img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_8/results/non_max_suppression.PNG" width="100">
- [Canny Edge Detection Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_8/src/canny_edge_detection.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_8/results)
```sh
python src/method_8/src/canny_edge_detection.py
```

## 9. Gaussian Pyramid & Laplacian Pyramid Filter
<p float="left">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_9/results/four_level_gaussian_pyramid.PNG" width="100">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_9/results/four_level_laplacian_pyramid.PNG" width="100">
</p>
- [Gaussian and Laplacian Pyramid Filter Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_9/src/gauss_laplace_pyramid.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_9/results)
```sh
python src/method_9/src/gauss_laplace_pyramid.py
```

## 10. Gaussian & Laplacian Pyramid Blend
<p float="left">
    <img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_10/results/gaussian_laplacian_pyramid_blend.PNG" width="100">
</p>
- [Gaussian & Laplacian Pyramid Blend Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_10/src/gauss_laplace_pyramid_blend.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_10/results)
```sh
python src/method_10/src/gauss_laplace_pyramid_blend.py
```

## 11. Ideal & Gaussian Bandpass Filters
<img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_11/results/gaussian_bandpass_filter.PNG" width="100">
<img src="https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_11/results/ideal_bandpass_filter.PNG" width="100">
- [Ideal Bandpass Filter Code](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_11/src/ideal_bandpass_filter)
- [Gaussian Bandpass Filter Code](https://github.com/mnguyen0226/dip_algorithms/blob/main/src/method_11/src/gaussian_bandpass_filter/gaussian_bandpass_filter.py)
- [Results](https://github.com/mnguyen0226/dip_algorithms/tree/main/src/method_11/results)
```sh
python src/method_11/src/gaussian_bandpass_filter/gaussian_bandpass_filter.py
python src/method_11/src/ideal_bandpass_filter/ideal_bandpass_filter.py
```



