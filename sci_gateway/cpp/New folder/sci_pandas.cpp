#include "function.hxx"
#include "string.hxx"
#include "PyVar.hxx"

extern "C" {
#include "Scierror.h"
#include "localization.h"
}

using namespace types;

types::Function::ReturnValue sci_pandas(types::typed_list& in, int _iRetCount, types::typed_list& out) {
	if(in.size()!=0){
		Scierror(999,"pandas:No arguments expected");
		return types::Function::Error;
	}
	if(Py_IsInitialized());
	else
		Py_Initialize();
	PyObject *output = PyImport_ImportModule("pandas");
	if (output == NULL) {
		Py_DECREF(output);
		Scierror(999,"pandas: Error while importing pandas. Check installation");
		return types::Function::Error;
	}
	
	PyVar *pOut = new PyVar(output);	
	out.push_back(pOut);
	return types::Function::OK;
}
