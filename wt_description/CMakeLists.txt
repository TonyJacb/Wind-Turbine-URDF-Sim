cmake_minimum_required(VERSION 3.0.2)
project(wt_description)

set(CMAKE_CXX_STANDARD 14)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  geometry_msgs
  tf2
  tf2_geometry_msgs
  urdf
  controller_manager
  joint_state_controller
  robot_state_publisher
)


catkin_package(
  CATKIN_DEPENDS
      roscpp
      geometry_msgs
      tf2
      tf2_geometry_msgs
      urdf
      controller_manager
      joint_state_controller
      robot_state_publisher
)

include_directories(
  ${catkin_INCLUDE_DIRS}
  include
)

add_executable(windStart 
              nodes/anemometer/windStart.cpp)

target_link_libraries(windStart 
                      ${catkin_LIBRARIES})
