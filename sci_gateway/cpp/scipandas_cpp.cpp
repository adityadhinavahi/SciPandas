#include "context.hxx"
#include "cpp_gateway_prototype.hxx"
#include "scipandas_cpp.hxx"
extern "C"
{
#include "scipandas_cpp.h"
}

#define MODULE_NAME L"scipandas_cpp"

int scipandas_cpp(wchar_t* _pwstFuncName)
{
    if(wcscmp(_pwstFuncName, L"pandas") == 0){ symbol::Context::getInstance()->addFunction(types::Function::createFunction(L"pandas", &sci_Pandas, MODULE_NAME)); }

    return 1;
}
