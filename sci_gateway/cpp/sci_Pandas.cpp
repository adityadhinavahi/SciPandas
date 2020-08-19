#include "function.hxx"
#include "string.hxx"
#include "PyVar.hxx"

extern "C" {
#include "Scierror.h"
#include "localization.h"
}

using namespace types;

types::Function::ReturnValue sci_Pandas(types::typed_list& in, int _iRetCount, types::typed_list& out) {
	PyObject *main, *globalDictionary, *localDictionary;
	if(!Py_IsInitialized()) {
		Py_Initialize();
		PyRun_SimpleString("import pandas as pd");
		main = PyImport_AddModule("__main__");
		globalDictionary = PyModule_GetDict(main);
		localDictionary = PyDict_New();

	}
	
	if(in.size() !=1){
		Scierror(999,"pythonic_pandas: Wrong Number of input arguments, One expected");
		return types::Function::Error;
	}

	if(_iRetCount > 1) {
		Scierror(999,"pythonic_pandas: Wrong number of output arguments, 1 expected");
		return types::Function::Error;
	}

	/*PyObject *module_imp = PyImport_ImportModule("pythonic_func");
	if(module_imp == NULL){
		Scierror(999,"pythonic_pandas: Couldn't import module");
		return types::Function::Error;
	}*/
	int a;
	std::cin>>a;
	std::cout<<a;
	types::String *pIn = in[0]->getAs<types::String>();
    wchar_t **winput = pIn -> get();
    char *input = new char[wcslen(*winput) + 1];
    sprintf(input, "%ws", *winput);
	PyObject *prun = PyRun_String(input,Py_file_input,globalDictionary,localDictionary);
	PyObject *orep = PyObject_Repr(prun);
    PyObject* str = PyUnicode_AsEncodedString(orep, "utf-8", "~E~");
	Py_DECREF(prun);
	const char  *output = PyBytes_AS_STRING(str);
	Py_DECREF(orep);
	Py_DECREF(str);
	//PyObject *newTuple = PyTuple_New(in.size());
	//if(l == NULL){
		//Scierror(999,"pythonic_pandas: Couldn't initialize'");
		//return types::Function::Error;
	//}
	//Py_DECREF(newTuple);
	//PyVar pOut = PyVar(l);
	out.push_back(new String(output));
	return types::Function::OK;
}