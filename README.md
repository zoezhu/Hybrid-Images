# Hybrid-Images
Hybrid two pictures, with one in a high frequency while another one in a low frequency.

In this code, for example, I use two pictures of myself to combine. An important thing is thant these two pictures are better have similar center of people or objects and similar color is also good. If we do have those two similar pictures, the result will be perfect to see only high frequency one when we take a close look, and low freqency one when we look at it in steps.


* Key Method: Impliment the first picture with laplacian pyramid, while the second one with Gaussian pyramid

* Principle: The difference between laplacian pyramid and Gaussian pyramid is that, the first one is calculated based on the seconde one, when we shrink a picture by half, the picture losses half of its information, we continue to shirnk it, we get a pyramid of pictures with less information, that is Gaussian pyramid. (Then we amplify the pictures to original size, the total imformation is the same as the small one. So the picture stays at low frequency which is blur.) Based on Gaussian pyramid, if we use original picture substracts the later one which contains less information we will get lossed information and that will be the lines of the picture which is high frequency, and that groups of substractions constitude laplacian pyramid.
