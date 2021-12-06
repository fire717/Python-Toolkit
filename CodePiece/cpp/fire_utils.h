
#define LINUX  

#include <fstream>
#include <iostream>

//win
// #include <direct.h> 
// #define OS_SEP "\\"

//linux
#ifdef LINUX  
#include <dirent.h>
#include <unistd.h>
#include <sys/stat.h>
#define OS_SEP "/"
#endif


static inline bool endsWith(const std::string& str, const std::string& end){
    int src_len = str.size();
    int end_len = end.size();
    if(src_len >= end_len){
        std::string temp = str.substr(src_len - end_len, end_len);
        if(temp == end)
            return true;
    }
    return false;
}


static inline void strReplace( std::string &str_origin, const std::string &str_src, const std::string &str_dst){
    std::string::size_type pos = 0;
    std::string::size_type src_len = str_src.size();
    std::string::size_type dst_len = str_dst.size();

    while( (pos=str_origin.find(str_src, pos)) != std::string::npos ){
        str_origin.replace( pos, src_len, str_dst );
        pos += dst_len;
    }
}


static inline std::string getBasename(std::string path){
    if (path.empty()){
        return "";
    }

    // strReplace(path, "/", "\\");
    // std::string::size_type iPos = path.find_last_of('\\') + 1;

    std::string::size_type iPos = path.find_last_of(OS_SEP) + 1;
    return path.substr(iPos, path.length() - iPos);
}
