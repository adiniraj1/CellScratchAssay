import matplotlib.pyplot as plt
from skimage import io
from skimage.filters.rank import entropy   # to separate the disturbed area(with cells) from non-disturbed area
from skimage.morphology import disk
from skimage.filters import threshold_otsu   # to have the entire segmentation/separation between two areas
import numpy as np                           # for mathematical use
import glob
# from scipy.stats import linregress
# for slope, intercept, r_value





t = 0
t_list= []                                        # list of time
area_list = []                                # list of scratched area with time
path = "images/*.*"                           # location of the stored images


for images in glob.glob(path):                 # for loop to access every image inside our path
    img = io.imread(images, as_gray= True)          # loading the image
    entropy_img = entropy(img,disk(10))               # making the entropy
    threshold= threshold_otsu(entropy_img)            # finding the threshold value for the segmentation
    binary = entropy_img<=threshold                   # converting the obtained value to the image
    t_list.append(t)                                  # making the time list
    t+=1
    area= np.sum(binary == True)                      # area of the whitespace (without cell) in the figure
    area_list.append(area)
    print(t, area)


plt.plot(t_list, area_list,'bo--')  # plotting the graph with t on x axis and area on y axis, go= green dots
plt.title('Scratched area Vs time')
plt.xlabel('time')
plt.ylabel('area of scratched part')
plt.text(0.75,30000,"y= -12048.5x + 31595.833333333332\nR^2 = 0.9979167160231691")
plt.show()


# print(linregress(t_list,area_list))

# slope, intercept, r_value, p_value, std_err = linregress(t_list, area_list)

# print("y= " + str(slope)+"x + "+str(intercept))
# print("R^2 value = " + str(pow(r_value, 2)))











