# Image-Dehazing-using-CNN

Images taken in foggy or hazy weather circumstances can be acutely affected by
scattering of atmospheric particles, which reduces the contrast, modifies the colour,
and makes the object features diffcult to identify by human vision and by some
outdoor computer vision systems. Hence, image dehazing is a vital problem and has
been widely researched in the domain of computer vision. The role of image
dehazing is to lessen the impact of weather elements to enhance the visual effects
of the image and give assistance to post processing of the image. This seminar
reviews the main methods of image dehazing that have been developed over the
past decade and explores a technique using Ranking CNN to automatically learn
haze relevant features which can be used to dehaze input hazy image.

By training RankingCNN in a well-designed manner, powerful haze-relevant features
can be automatically learned from massive hazy image patches.
Based on these features, haze can be effectively removed by using
a haze density prediction model trained through the random
forest regression.
