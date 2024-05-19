// Generated by gencpp from file morai_msgs/FaultInjection_Controller.msg
// DO NOT EDIT!


#ifndef MORAI_MSGS_MESSAGE_FAULTINJECTION_CONTROLLER_H
#define MORAI_MSGS_MESSAGE_FAULTINJECTION_CONTROLLER_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace morai_msgs
{
template <class ContainerAllocator>
struct FaultInjection_Controller_
{
  typedef FaultInjection_Controller_<ContainerAllocator> Type;

  FaultInjection_Controller_()
    : unique_id(0)
    , fault_location(0)
    , fault_class(0)
    , fault_subclass(0)  {
    }
  FaultInjection_Controller_(const ContainerAllocator& _alloc)
    : unique_id(0)
    , fault_location(0)
    , fault_class(0)
    , fault_subclass(0)  {
  (void)_alloc;
    }



   typedef int32_t _unique_id_type;
  _unique_id_type unique_id;

   typedef int32_t _fault_location_type;
  _fault_location_type fault_location;

   typedef int32_t _fault_class_type;
  _fault_class_type fault_class;

   typedef int32_t _fault_subclass_type;
  _fault_subclass_type fault_subclass;





  typedef boost::shared_ptr< ::morai_msgs::FaultInjection_Controller_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::morai_msgs::FaultInjection_Controller_<ContainerAllocator> const> ConstPtr;

}; // struct FaultInjection_Controller_

typedef ::morai_msgs::FaultInjection_Controller_<std::allocator<void> > FaultInjection_Controller;

typedef boost::shared_ptr< ::morai_msgs::FaultInjection_Controller > FaultInjection_ControllerPtr;
typedef boost::shared_ptr< ::morai_msgs::FaultInjection_Controller const> FaultInjection_ControllerConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::morai_msgs::FaultInjection_Controller_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::morai_msgs::FaultInjection_Controller_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::morai_msgs::FaultInjection_Controller_<ContainerAllocator1> & lhs, const ::morai_msgs::FaultInjection_Controller_<ContainerAllocator2> & rhs)
{
  return lhs.unique_id == rhs.unique_id &&
    lhs.fault_location == rhs.fault_location &&
    lhs.fault_class == rhs.fault_class &&
    lhs.fault_subclass == rhs.fault_subclass;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::morai_msgs::FaultInjection_Controller_<ContainerAllocator1> & lhs, const ::morai_msgs::FaultInjection_Controller_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace morai_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::morai_msgs::FaultInjection_Controller_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::morai_msgs::FaultInjection_Controller_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::morai_msgs::FaultInjection_Controller_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::morai_msgs::FaultInjection_Controller_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::morai_msgs::FaultInjection_Controller_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::morai_msgs::FaultInjection_Controller_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::morai_msgs::FaultInjection_Controller_<ContainerAllocator> >
{
  static const char* value()
  {
    return "29fcfb33853ca6e2114fbfdf30c06eaf";
  }

  static const char* value(const ::morai_msgs::FaultInjection_Controller_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x29fcfb33853ca6e2ULL;
  static const uint64_t static_value2 = 0x114fbfdf30c06eafULL;
};

template<class ContainerAllocator>
struct DataType< ::morai_msgs::FaultInjection_Controller_<ContainerAllocator> >
{
  static const char* value()
  {
    return "morai_msgs/FaultInjection_Controller";
  }

  static const char* value(const ::morai_msgs::FaultInjection_Controller_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::morai_msgs::FaultInjection_Controller_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 unique_id\n"
"\n"
"int32 fault_location\n"
"int32 fault_class\n"
"int32 fault_subclass\n"
;
  }

  static const char* value(const ::morai_msgs::FaultInjection_Controller_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::morai_msgs::FaultInjection_Controller_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.unique_id);
      stream.next(m.fault_location);
      stream.next(m.fault_class);
      stream.next(m.fault_subclass);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct FaultInjection_Controller_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::morai_msgs::FaultInjection_Controller_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::morai_msgs::FaultInjection_Controller_<ContainerAllocator>& v)
  {
    s << indent << "unique_id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.unique_id);
    s << indent << "fault_location: ";
    Printer<int32_t>::stream(s, indent + "  ", v.fault_location);
    s << indent << "fault_class: ";
    Printer<int32_t>::stream(s, indent + "  ", v.fault_class);
    s << indent << "fault_subclass: ";
    Printer<int32_t>::stream(s, indent + "  ", v.fault_subclass);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MORAI_MSGS_MESSAGE_FAULTINJECTION_CONTROLLER_H