#include "context.hxx"
#include "cpp_gateway_prototype.hxx"
#include "scithon_cpp.hxx"
extern "C"
{
#include "scithon_cpp.h"
}

#define MODULE_NAME L"scithon_cpp"

int scithon_cpp(wchar_t* _pwstFuncName)
{
    if(wcscmp(_pwstFuncName, L"pandas") == 0){ symbol::Context::getInstance()->addFunction(types::Function::createFunction(L"pandas", &sci_pandas, MODULE_NAME)); }
    if(wcscmp(_pwstFuncName, L"PythonicPandas") == 0){ symbol::Context::getInstance()->addFunction(types::Function::createFunction(L"PythonicPandas", &sci_PythonicPandas, MODULE_NAME)); }
    if(wcscmp(_pwstFuncName, L"show") == 0){ symbol::Context::getInstance()->addFunction(types::Function::createFunction(L"show", &sci_show, MODULE_NAME)); }

    return 1;
}
