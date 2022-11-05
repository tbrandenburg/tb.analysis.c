# tb.analysis.c

Parses a given folder recursively for C and H files and turning their
AST into a JSON

## Sample output

~~~json
{
    "test": {
        "is_dir": true,
        "children": {
            "main.c": {
                "is_dir": false,
                "size": 20,
                "AST": {
                    "variables": {},
                    "functions": {
                        "main": {
                            "line": 1,
                            "return": "void"
                        }
                    }
                }
            },
            "test.c": {
                "is_dir": false,
                "size": 187,
                "AST": {
                    "variables": {
                        "privateVar": {
                            "line": 6,
                            "type": "int"
                        }
                    },
                    "functions": {
                        "getBar": {
                            "line": 12,
                            "parameters": {
                                "0": "int",
                                "1": "int"
                            },
                            "return": "int"
                        },
                        "getFoo": {
                            "line": 8,
                            "return": "int"
                        }
                    }
                }
            },
            "test.h": {
                "is_dir": false,
                "size": 124,
                "AST": {
                    "variables": {
                        "globalVar": {
                            "line": 5,
                            "type": "int"
                        }
                    },
                    "functions": {
                        "getBar": {
                            "line": 9,
                            "parameters": {
                                "0": "int",
                                "1": "int"
                            },
                            "return": "int"
                        },
                        "getFoo": {
                            "line": 7,
                            "return": "int"
                        }
                    }
                }
            }
        }
    }
}
~~~
