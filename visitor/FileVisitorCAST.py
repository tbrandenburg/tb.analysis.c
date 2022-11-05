import os
import subprocess
import json

from FileVisitor import *

class FileVisitorCAST(FileVisitor):

    def visit(self,isDir,relFilePath,absFilePath,fileName) -> bool:
        if not isDir:
            print("[FileVisitorCAST] Parsing " + relFilePath + "...")
            result = subprocess.run(['java', '-jar', 'utils/CParser.jar', absFilePath], stdout=subprocess.PIPE)
            return {"AST":json.loads(result.stdout.decode("utf-8"))}
        return dict()