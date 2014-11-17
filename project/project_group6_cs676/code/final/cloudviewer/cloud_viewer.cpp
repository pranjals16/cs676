#include <pcl/visualization/cloud_viewer.h>
#include <iostream>
#include <pcl/io/io.h>
#include <pcl/io/pcd_io.h>
    
int 
main (int argc, char** argv)
{
    if(argc != 2) {
      std::cout << "Usage : " << argv[0] << " <cloud_file.pcd>\n";
      return 1;
    }
    pcl::PointCloud<pcl::PointXYZRGBA>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZRGBA>);
    pcl::io::loadPCDFile (argv[1], *cloud);
    
    pcl::visualization::CloudViewer viewer("Cloud Viewer");
    
    //blocks until the cloud is actually rendered
    viewer.showCloud(cloud);

    while(!viewer.wasStopped())
    {
    }
 
    return 0;
}
