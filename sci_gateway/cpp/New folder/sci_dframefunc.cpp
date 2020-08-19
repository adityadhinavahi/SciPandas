#include "function.hxx"
#include "string.hxx"
#include "PyVar.hxx"

extern "C" {
#include "Scierror.h"
#include "localization.h"
}

using namespace types;

types::Function::ReturnValue sci_dframefunc(types::typed_list& in, int _iRetCount, types::typed_list& out) {
	if(!Py_IsInitialized()) {
		Scierror(999,"pythonic_pandas: Python instance is down, call pandas");
		return types::Function::Error;
	}
	
	if(in.size() !=1){
		Scierror(999,"pythonic_pandas: Wrong Number of input arguments, one expected");
		return types::Function::Error;
	}
	
	
	if(_iRetCount > 1) {
		Scierror(999,"pythonic_pandas: Wrong number of output arguments, 1 expected");
		return types::Function::Error;
	}
	if(in[0] -> getTypeStr() != L"Python Variable"){
		Scierror(999,"pythonic_pandas: Wrong argument expected a dataframe variable");
		return types::Function::Error;
	}
	PyVar df = PyVar(in[0]);
	PyObject *newTuple = PyTuple_New(in.size());
	PyTuple_SetItem(newTuple,0, df.get());
    //PyObject* sysPath = PySys_GetObject("path");
    //PyRun_SimpleString("import os");
    //PyRun_SimpleString("os.getcwd()");
    //PyList_Append(sysPath, PyUnicode_FromString("F:\\downloads\\Scithon-v0.1.12_c\\Scithon-v0.1.12_c\\sci_gateway\\Python"));
	PyObject *module_imp = PyImport_ImportModule("pythonic_func");
	if(module_imp == NULL){
		Scierror(999,"pythonic_pandas: Couldn't import module");
		return types::Function::Error;
	}
	PyObject *pclass = PyObject_GetAttrString(module_imp,"dframe");
	Py_DECREF(module_imp);
	PyObject *l = PyObject_CallObject(pclass,newTuple);
	if(l==NULL){
		Scierror(999,"pythonic_pandas: Couldn't get pythonic_pandas from given object. Did you pass a DataFrame Object");
		return types::Function::Error; }
	Py_DECREF(newTuple);
	PyVar *pOut = new PyVar(l);
	out.push_back(pOut);
	return types::Function::OK;
}
	
