class adp_os_filenames():
    
    def pic_rename(list):
        """
        データの名前を適切にして返す
        """
        import numpy as np
        done=[]
        for i in range(len(list)):
            content=re.split('[.,_]',list[i])
            dname=content[0]
            num=content[1].zfill(4)
            ext=content[2]
            done.append('.'.join(['_'.join([dname,num]), ext]))
        return np.array(done)

    def replace_dic(dic):
        """
        辞書型データ１をコピーして、データの名前を適切にして辞書型データ２に返す
        """
        import copy
        dic2=dic.copy()
        for i in dic2.keys():
            if 'input'==i:
                continue
            else:
                dic2[i]=pic_rename(dic2[i])
        return dic2

    def os_rename(dic1, dic2):
        """
        ストレージにあるファイル名の変更
        """
        import os
        for i in dic1:
            if i!='input':
                for j, k in zip(dic1[i],dic2[i]):
                    os.rename(i+"/"+j,i+"/"+k)
            else:
                continue
        return