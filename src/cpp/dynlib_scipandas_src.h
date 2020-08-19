#ifndef __DYNLIB_SCIPANDAS_SRC_H__
#define __DYNLIB_SCIPANDAS_SRC_H__

#ifdef _MSC_VER
#ifdef SCIPANDAS_EXPORTS
#define SCIPANDAS_SRC_IMPEXP __declspec(dllexport)
#else
#define SCIPANDAS_SRC_IMPEXP __declspec(dllimport)
#endif
#else
#define SCIPANDAS_SRC_IMPEXP
#endif

#endif
