# Hybrid-Images
Hybrid two pictures, with one in a high frequency while another one in a low frequency.

In this code, for example, I use two pictures of myself to combine. An important thing is thant these two pictures are better have similar center of people or objects and similar color is also good. If we do have those two similar pictures, the result will be perfect to see only high frequency one when we take a close look, and low freqency one when we look at it in steps.


* <b>Key Method</b>: Impliment the first picture with laplacian pyramid, while the second one with Gaussian pyramid

* <b>Principle</b>: The difference between <b>laplacian pyramid</b> and <b>Gaussian pyramid</b> is that, the first one is calculated based on the seconde one, when we shrink a picture by half, the picture losses half of its information, we continue to shirnk it, we get a pyramid of pictures with less information, that is Gaussian pyramid. (Then we amplify the pictures to original size, the total imformation is the same as the small one. So the picture stays at low frequency which is blur.) Based on Gaussian pyramid, if we use original picture substracts the later one which contains less information we will get lossed information and that will be the lines of the picture which is high frequency, and that groups of substractions constitude laplacian pyramid.



The whole idea comes from the paper: Oliva, A., Torralba, A., & Schyns, P. G. (2006, July). Hybrid images. In ACM Transactions on Graphics (TOG) (Vol. 25, No. 3, pp. 527-532). ACM.
