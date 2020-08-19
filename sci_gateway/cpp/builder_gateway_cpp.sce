function builder_gateway_cpp()
    gwPath = get_absolute_file_path("builder_gateway_cpp.sce");
    origPath = pwd();
    //cd(gwPath);
    gw_table = [
        "pandas", "sci_Pandas", "cppsci";
    ];

    CFLAGS = ilib_include_flag(gwPath);
    CFLAGS = ilib_include_flag(fullpath(gwPath + "../../src/c"));
    CFLAGS = CFLAGS + " " + ilib_include_flag(fullpath(gwPath + "../../src/cpp"));
    CFLAGS = CFLAGS + " " + ilib_include_flag(fullpath(gwPath + "../../python/include"));
    CFLAGS = CFLAGS + " " + ilib_include_flag(fullpath(SCI + "/modules/ast/includes"));

    LDFLAGS = fullpath(gwPath + "../../src/c/libPythonInstance.lib");
    LDFLAGS = LDFLAGS + " " + fullpath(gwPath + "../../src/cpp/libPyVar.lib");
    LDFLAGS = LDFLAGS + " " + fullpath(gwPath + "../../python/libs/python38.lib");

    gw_src_cpp = [
        "sci_Pandas.cpp";
    ];

    //WITHOUT_AUTO_PUTLHSVAR = %t;
    //disp(CFLAGS);
    tbx_build_gateway("scipandas_cpp", gw_table, gw_src_cpp, gwPath, ["../../src/c/libPythonInstance"], LDFLAGS, CFLAGS);
    //cd(origPath);
endfunction

builder_gateway_cpp();
clear builder_gateway_cpp;
