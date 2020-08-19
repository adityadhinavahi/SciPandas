#ifndef __SCITHON_CPP_GW_HXX__
#define __SCITHON_CPP_GW_HXX__

#ifdef _MSC_VER
#ifdef SCITHON_CPP_GW_EXPORTS
#define SCITHON_CPP_GW_IMPEXP __declspec(dllexport)
#else
#define SCITHON_CPP_GW_IMPEXP __declspec(dllimport)
#endif
#else
#define SCITHON_CPP_GW_IMPEXP
#endif

extern "C" SCITHON_CPP_GW_IMPEXP int scithon_cpp(wchar_t* _pwstFuncName);

CPP_GATEWAY_PROTOTYPE(sci_PythonicPandas);
CPP_GATEWAY_PROTOTYPE(sci_pandas);
CPP_GATEWAY_PROTOTYPE(sci_show);

#endif /* __SCITHON_CPP_GW_HXX__ */
