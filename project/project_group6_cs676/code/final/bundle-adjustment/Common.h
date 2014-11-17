#include <opencv2/core/core.hpp>
#include <opencv2/features2d/features2d.hpp>
#include <vector>

struct CloudPoint {
	cv::Point3d pt;
	std::vector<int> imgpt_for_img;
	double reprojection_error;
};

