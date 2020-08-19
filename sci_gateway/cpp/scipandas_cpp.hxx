#ifndef __SCIPANDAS_CPP_GW_HXX__
#define __SCIPANDAS_CPP_GW_HXX__

#ifdef _MSC_VER
#ifdef SCIPANDAS_CPP_GW_EXPORTS
#define SCIPANDAS_CPP_GW_IMPEXP __declspec(dllexport)
#else
#define SCIPANDAS_CPP_GW_IMPEXP __declspec(dllimport)
#endif
#else
#define SCIPANDAS_CPP_GW_IMPEXP
#endif

extern "C" SCIPANDAS_CPP_GW_IMPEXP int scipandas_cpp(wchar_t* _pwstFuncName);

CPP_GATEWAY_PROTOTYPE(sci_Pandas);

#endif /* __SCIPANDAS_CPP_GW_HXX__ */
