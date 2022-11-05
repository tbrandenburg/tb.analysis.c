import os
import subprocess
import json

import time

import threading

# py4j is mainly used to improve performance by loading java class and Eclipse
# CDT only once
from py4j.java_gateway import JavaGateway

from FileVisitor import *

class FileVisitorCAST(FileVisitor):

    # Private CParser object
    __cp = None

    def __py4j_gateway(self):
        result = subprocess.run(['java', '-jar', 'utils/CParser.jar'], stdout=subprocess.PIPE)
    
    def __init__(self):

        print("[FileVisitorCAST] Starting py4j gateway...")

        # Start py4j gateway in a thread because it is blocking
        thread = threading.Thread(target=self.__py4j_gateway, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()

        # Wait for py4j gateway
        time.sleep(1)

        try:
            gateway = JavaGateway()
            self.__cp = gateway.entry_point
            print("[FileVisitorCAST] Connected to py4j gateway!")
        except:
            print("[FileVisitorCAST] [Error] Connection to py4j gateway could not be established!")

    def visit(self,isDir,relFilePath,absFilePath,fileName) -> bool:
        if not isDir:
            if(self.__cp):
                # Read file
                with open(absFilePath, "r") as f:
                    code = f.read()
                    f.close()

                # Parse file!
                print("[FileVisitorCAST] Parsing " + absFilePath + "...")
                self.__cp.parse(absFilePath, code)

                # Convert to AST to JSON
                jsonStr = str(self.__cp.toJSON().toString())
                return {"AST":json.loads(jsonStr)}
        return dict()