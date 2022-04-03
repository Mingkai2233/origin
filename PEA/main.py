# object
class ImageDataDirectory:
    def __init__(self, rva, size):
        self.Rva = rva
        self.Size = size


class ImageImportDescriptor:  # 存储导入表的各项信息
    def __init__(self, begin_address, offset):
        self.OriginalFirstThunk = rawhex_to_hex(peFile[begin_address:begin_address + 4])  # 需要用offset修正
        self.TimeDataStamp = rawhex_to_hex(peFile[begin_address + 4:begin_address + 8])
        self.ForwarderChain = rawhex_to_hex(peFile[begin_address + 8: begin_address + 0xc])
        self.Name = rawhex_to_hex(peFile[begin_address + 0xc:begin_address + 0x10])  # 名字的指针需要用offset修正
        self.FirstThunk = rawhex_to_hex(peFile[begin_address + 0x10:begin_address + 0x14])
        self.offset = offset
        self.functionList = []

    def __str__(self):
        return 'Name: ' + self.get_name() + '\n' + \
               'TimeDataStamp: ' + self.TimeDataStamp + '\n' + \
               'ForwarderChain: ' + self.ForwarderChain + '\n' + \
               'OriginalFirstThunk: ' + self.OriginalFirstThunk + '\n' + \
               'FirstThunk: ' + self.FirstThunk + '\n'

    def get_name(self):
        ad = int(self.Name, 16) - int(self.offset, 16)
        for i in range(50):
            tmp = peFile[ad + i]
            if tmp == 0:
                break
        name = peFile[ad:ad + i]
        return name.decode()

    def isnull(self):
        if int(self.OriginalFirstThunk, 16) == 0:
            return True
        else:
            return False


class ImageSectionHeader:
    def __init__(self, begin_address, peFile):
        ad = begin_address
        self.Name = peFile[ad:ad + 8]
        self.VirtualSize = rawhex_to_hex(peFile[ad + 8:ad + 12])  # 区块的尺寸
        self.VirtualAddress = rawhex_to_hex(peFile[ad + 12:ad + 16])  # 区块的RVA
        self.SizeOfRawData = rawhex_to_hex(peFile[ad + 16:ad + 20])  # 区块文件中对齐后的尺寸
        self.PointerToRawData = rawhex_to_hex(peFile[ad + 20:ad + 24])  # 在文件中的偏移
        self.PointerToRelocations = rawhex_to_hex(peFile[ad + 24:ad + 28])
        self.PointerToLinenumbers = rawhex_to_hex(peFile[ad + 28:ad + 32])
        self.NumberOfRelocation = rawhex_to_hex(peFile[ad + 32:ad + 34])
        self.NumberOfLinenumbers = rawhex_to_hex(peFile[ad + 34:ad + 36])
        self.Characteristics = rawhex_to_hex(peFile[ad + 36:ad + 40])

    def __str__(self):
        list1 = list(self.Name)
        name = ''
        for i in list1:
            name = name + chr(i)
        return 'Name:' + name + '\n' + \
               'VirtualSize: ' + self.VirtualSize + '\n' + \
               'VirtualAddress: ' + self.VirtualAddress + '\n' + \
               'SizeOfRawData: ' + self.SizeOfRawData + '\n' + \
               'PointerToRawData: ' + self.PointerToRawData + '\n' + \
               'PointerToRelocation: ' + self.PointerToRelocations + '\n' + \
               'PointerToLinenumbers: ' + self.PointerToLinenumbers + '\n' + \
               'NumberOfRelocation: ' + self.NumberOfRelocation + '\n' + \
               'NumberOfLinenumbers: ' + self.NumberOfLinenumbers + '\n' + \
               'Characteristics: ' + self.Characteristics + '\n'


class Function:
    def __init__(self, hint, name):
        self.hint = hint
        self.name = name


class DataEntry:
    def __init__(self, file, ad, offset=0):
        self.OffsetToData = rawhex_to_hex(file[ad:ad + 4])
        self.Size = rawhex_to_hex(file[ad + 4:ad + 8])
        self.CodePage = rawhex_to_hex(file[ad + 8:ad + 12])
        self.Reserved = rawhex_to_hex(file[ad + 12:ad + 16])
        self.offset = offset

    def __str__(self):
        return "OffsetToData: " + self.OffsetToData + \
               ' | Size: ' + self.Size + \
               ' | CodePage: ' + self.CodePage + \
               ' | Reserved: ' + self.Reserved


class DirEntry:
    def __init__(self, file, beginad, originalad):
        self.tmpName = rawhex_to_hex(file[beginad:beginad + 4])
        self.OffsetToData = rawhex_to_hex(file[beginad + 4:beginad + 8])
        self.Id = 'None'
        self.Name = 'None'
        self.nextnode = None
        self.dataEntry = None

        tmp = int(self.tmpName, 16) - int('0x80000000', 16)
        if tmp > 0:
            nameLength = int(rawhex_to_hex(file[originalad + tmp:originalad + tmp + 2]), 16) * 2
            self.Name = file[originalad + tmp + 2:originalad + tmp + 2+nameLength].decode()
        else:
            self.Id = self.tmpName

    def __str__(self):
        return "Id:" + self.Id + \
               " | OffsetToData:" + self.OffsetToData +\
               " | Name:" + self.Name


class ResourceNode:
    def __init__(self, file, beginad: int, originalad: int):
        self.originalad = originalad
        self.file = file

        self.Characteristics = rawhex_to_hex(file[beginad:beginad + 4])
        self.TimeDateStamp = rawhex_to_hex(file[beginad + 4:beginad + 8])
        self.MajorVersion = rawhex_to_hex(file[beginad + 8:beginad + 10])
        self.MinorVersion = rawhex_to_hex(file[beginad + 10:beginad + 12])
        self.NumberOfNamedEntries = rawhex_to_hex(file[beginad + 12:beginad + 14])
        self.NumberOfIdEntries = rawhex_to_hex(file[beginad + 14:beginad + 16])
        self.entries = []

        ad = beginad + 16
        for i in range(int(self.NumberOfIdEntries, 16) + int(self.NumberOfNamedEntries, 16)):
            self.entries.append(DirEntry(self.file, ad + i * 8, self.originalad))

    def get_next_node(self):
        for i in self.entries:
            tmp = int(i.OffsetToData, 16) - int('0x80000000', 16)
            if tmp > 0:
                i.nextnode = ResourceNode(self.file, self.originalad + tmp, self.originalad)
            else:
                i.dataEntry = DataEntry(self.file, self.originalad + int(i.OffsetToData, 16))

    def __str__(self):
        return 'NumberOfNamedEntries: ' + self.NumberOfNamedEntries +\
               ' | NumberOfIdEntries: ' + self.NumberOfIdEntries + \
                ' | Characteristics: ' + self.Characteristics + \
                ' | TimeDateStamp: ' + self.TimeDateStamp + \
                ' | MajorVersion: ' + self.MajorVersion + \
                ' | MinorVersion: ' + self.MinorVersion


class ImageExportTable:
    def __init__(self, file, ad: int, offset: int):
        self.Characteristics = rawhex_to_hex(file[ad:ad+4])
        self.TimeDateStamp = rawhex_to_hex(file[ad+4:ad+8])
        self.MajorVersion = rawhex_to_hex(file[ad+8:ad+10])
        self.MinorVersion = rawhex_to_hex(file[ad+10:ad+12])
        self.Name = rawhex_to_hex(file[ad+12:ad+16])
        self.Base = rawhex_to_hex(file[ad+16:ad+20])
        self.NumberOfFunctions = rawhex_to_hex(file[ad+20:ad+24])
        self.NumberOfNames = rawhex_to_hex(file[ad+24:ad+28])
        self.AddressOfFunctions = rawhex_to_hex(file[ad+28:ad+32])
        self.AddressOfNames = rawhex_to_hex(file[ad+32:ad+36])
        self.AddressOfNameOrdinals = rawhex_to_hex(file[ad+36:ad+40])
        self.offset = offset
        self.Addresses = []
        self.Names = []
        self.NameOrdinals = []
        # get name
        beginad = int(self.Name, 16) - offset
        for i in range(50):
            if file[beginad+i] == 0:
                break
        self.Name = file[beginad:beginad+i].decode()
        # get functions
        num = int(self.NumberOfFunctions, 16)
        beginad = int(self.AddressOfFunctions, 16) - offset
        for i in range(num):
            self.Addresses.append(rawhex_to_hex(file[beginad+i*4:beginad+4+4*i]))
        # get names
        num = int(self.NumberOfNames, 16)
        beginad = int(self.AddressOfNames, 16) - offset
        for i in range(num):
            namead = int(rawhex_to_hex(file[beginad:beginad+4]), 16)
            beginad += 4
            for j in range(50):
                if file[namead+j] == 0:
                    tmp = file[namead:namead+j].decode()
                    self.Names.append(tmp)
                    break
        # get nameoriginals
        beginad = int(self.AddressOfNameOrdinals, 16) - offset
        print(num)
        for i in range(num):
            tmp = rawhex_to_hex(file[beginad+i*2:beginad+i*2+2])
            self.NameOrdinals.append(tmp)


def rawhex_to_hex(string):  # 将内存中的字节码转为十六进制数字,以字符串形式返回
    list1 = list(string)
    for i in range(len(list1)):
        list1[i] = hex(list1[i])
    result = ''
    for i in range(1, len(list1) + 1):
        tmp = list1[-i][2:]
        if int(tmp, 16) < 16:
            tmp = '0' + tmp
        result += tmp
    return '0x' + result


def get_offset(sections: list, rva: str) -> str:  # 获得当前数据的rva和文件偏移量的差值
    rva = int(rva, 16)
    for i in range(len(sections) - 1):
        if (rva >= int(sections[i].VirtualAddress, 16) and rva < int(sections[i + 1].VirtualAddress, 16)):
            return hex(int(sections[i].VirtualAddress, 16) - int(sections[i].PointerToRawData, 16))
    i = len(sections) - 1
    return hex(int(sections[i].VirtualAddress, 16) - int(sections[i].PointerToRawData, 16))


def get_IID(ad, offset):
    listIID = list()
    ad = int(ad, 16)
    for i in range(100):
        listIID.append(ImageImportDescriptor(ad + i * 20, offset))
        if (listIID[i].isnull()):
            del listIID[i]
            return listIID


def get_rawoffset(rva, offset):
    return hex(int(rva, 16) - int(offset, 16))


def get_function_list(file, rva, offset):
    ad = int(get_rawoffset(rva, offset), 16)
    funcList = list()
    while True:
        tmp = rawhex_to_hex(file[ad:ad + 4])  # 此时存储的为originalFirstThunk的值
        ad = ad + 4
        if int(tmp, 16) == 0:
            break
        else:
            tmp = int(get_rawoffset(tmp, offset), 16)
            hint = rawhex_to_hex(file[tmp:tmp + 2])
            tmp += 2
            for i in range(100):
                if (file[tmp + i] == 0):
                    break
            name = file[tmp:tmp + i]
            name = name.decode()
            funcList.append(Function(hint, name))
    return funcList


def get_dosheader(file):
    tmpdict = dict()
    tmpdict['e_magic'] = rawhex_to_hex(file[0:0x2])
    tmpdict['e_cblp'] = rawhex_to_hex(file[0x2:0x4])
    tmpdict['e_cp'] = rawhex_to_hex(file[0x4:0x6])
    tmpdict['e_crlc'] = rawhex_to_hex(file[0x6:0x8])
    tmpdict['e_cparhdr'] = rawhex_to_hex(file[0x8:0x2])
    tmpdict['e_minalloc'] = rawhex_to_hex(file[0x0a:0xc])
    tmpdict['e_maxalloc'] = rawhex_to_hex(file[0xc:0xe])
    tmpdict['e_ss'] = rawhex_to_hex(file[0xe:0x10])
    tmpdict['e_sp'] = rawhex_to_hex(file[0x10:0x12])
    tmpdict['e_csum'] = rawhex_to_hex(file[0x12:0x14])
    tmpdict['e_ip'] = rawhex_to_hex(file[0x14:0x16])
    tmpdict['e_cs'] = rawhex_to_hex(file[0x16:0x18])
    tmpdict['e_lfarlc'] = rawhex_to_hex(file[0x18:0x1a])
    tmpdict['e_ovno'] = rawhex_to_hex(file[0x1a:0x1c])
    tmpdict['e_res'] = rawhex_to_hex(file[0x1c:0x24])
    tmpdict['e_oemid'] = rawhex_to_hex(file[0x24:0x26])
    tmpdict['e_oeminfo'] = rawhex_to_hex(file[0x26:0x28])
    tmpdict['e_res2'] = rawhex_to_hex(file[0x28:0x3c])
    tmpdict['e_lfanew'] = rawhex_to_hex(file[0x3c:0x40])
    return tmpdict


def get_fileheader(file):
    tmpdict = dict()
    tmpdict['Machine'] = rawhex_to_hex(file[4:0x6])
    tmpdict['NumberOfSection'] = rawhex_to_hex(file[0x6:0x8])
    tmpdict['TimeDateStamp'] = rawhex_to_hex(file[0x8:0xc])
    tmpdict['PointerToSymbolTable'] = rawhex_to_hex(file[0xc:0x10])
    tmpdict['NumberOfSymbols'] = rawhex_to_hex(file[0x10:0x14])
    tmpdict['SizeOfOptionalHeader'] = rawhex_to_hex(file[0x14:0x16])
    tmpdict['Characteristics'] = rawhex_to_hex(file[0x16:0x18])
    return tmpdict


def get_optional_header(file):
    tmpdict = dict()
    tmpdict['Magic'] = rawhex_to_hex(file[0x18:0x1a])
    tmpdict['MajorLinkerVersion'] = rawhex_to_hex(file[0x1a:0x1b])
    tmpdict['MinorLinkerVersion'] = rawhex_to_hex(file[0x1b:0x1c])
    tmpdict['SizeOfCode'] = rawhex_to_hex(file[0x1c:0x20])
    tmpdict['SizeOfInitializeData'] = rawhex_to_hex(file[0x20:0x24])
    tmpdict['SizeOfUninitializeData'] = rawhex_to_hex(file[0x24:0x28])
    tmpdict['AddressOfEntryPoint'] = rawhex_to_hex(file[0x28:0x2c])
    tmpdict['BaseOfCode'] = rawhex_to_hex(file[0x2c:0x30])
    tmpdict['BaseOfData'] = rawhex_to_hex(file[0x30:0x34])
    tmpdict['ImageBase'] = rawhex_to_hex(file[0x34:0x38])
    tmpdict['SectionAlignment'] = rawhex_to_hex(file[0x38:0x3c])
    tmpdict['FileAlignment'] = rawhex_to_hex(file[0x3c:0x40])
    tmpdict['MajorOperatingSystemVersion'] = rawhex_to_hex(file[0x40:0x42])
    tmpdict['MinorOperatingSystemVersion'] = rawhex_to_hex(file[0x42:0x44])
    tmpdict['MajorImageVersion'] = rawhex_to_hex(file[0x44:0x46])
    tmpdict['MinorImageVersion'] = rawhex_to_hex(file[0x46:0x48])
    tmpdict['MajorSubsystemVersion'] = rawhex_to_hex(file[0x48:0x4a])
    tmpdict['MinorSubsystemVersion'] = rawhex_to_hex(file[0x4a:0x4c])
    tmpdict['Win32VersionValue'] = rawhex_to_hex(file[0x4c:0x50])
    tmpdict['SizeOfImage'] = rawhex_to_hex(file[0x50:0x54])
    tmpdict['SizeOfHeaders'] = rawhex_to_hex(file[0x54:0x58])
    tmpdict['CheckSum'] = rawhex_to_hex(file[0x58:0x5c])
    tmpdict['Subsystem'] = rawhex_to_hex(file[0x5c:0x5e])
    tmpdict['DllCharacteristics'] = rawhex_to_hex(file[0x5e:0x60])
    tmpdict['SizeOfStackReserve'] = rawhex_to_hex(file[0x60:0x64])
    tmpdict['SizeOfStackCommit'] = rawhex_to_hex(file[0x64:0x68])
    tmpdict['SizeOfHeapReserve'] = rawhex_to_hex(file[0x6c:0x70])
    tmpdict['SizeOfHeapCommit'] = rawhex_to_hex(file[0x70:0x74])
    tmpdict['LoaderFlags'] = rawhex_to_hex(file[0x74:0x78])
    return tmpdict


# 主程序区
PATH1 = r'C:\Users\gr4y\Desktop\软件安全\软件安全实验2\TraceMe.exe'
PATH2 = r'C:\Users\gr4y\Desktop\软件安全\实验1\libzplay.dll'
with open(PATH2, 'rb') as f:
    peFile = f.read()

    # DOS头
    dict_dosHeader = get_dosheader(peFile)
    # PE文件头
    # -定位相关项
    signatureOffset = peFile[0x3c:0x40]
    signatureOffset = int(rawhex_to_hex(signatureOffset), 16)
    fileHeaderOffset = signatureOffset + 4
    ntHeader = peFile[signatureOffset:signatureOffset + 0xf8]
    # -收集相关项数据
    # --IMAGE_FILE_HEADER
    dict_fileHeader = get_fileheader(ntHeader)
    Signature = ntHeader[0:4:].decode
    # --IMAGE_FILE_OPTIONAL_HEADER
    dict_fileOptionalHeader = get_optional_header(ntHeader)
    # 块表
    peFileExceptDos = peFile[signatureOffset:]
    sectionList = list()
    begin = 0x78 + 0x80
    numberOfSection = int(dict_fileHeader['NumberOfSection'], 16)
    for i in range(numberOfSection):
        sectionList.append(ImageSectionHeader(begin + 40 * i, peFileExceptDos))
    # 其他部分
    # -定位,准备工作
    dict_dataDir = dict()
    dataName = ['Export Table', 'Import Table', 'Resources Table', 'Exception Table', 'Security Table',
                'Base relocation Table', 'Debug', 'Copyright', 'Global Ptr', 'Thread local storage',
                'Load configuration', 'Bound Import', 'Import Address Table', 'Delay Import', 'COM descriptor', 'other']
    for i in range(15):
        dataDirRva = rawhex_to_hex(ntHeader[0x78 + 0x8 * i:0x78 + 0x4 + 0x8 * i])
        dataDirSize = rawhex_to_hex(ntHeader[0x7c + 0x8 * i:0x7c + 0x4 + 0x8 * i])
        dict_dataDir[dataName[i]] = ImageDataDirectory(dataDirRva, dataDirSize)
    # -输入表
    importTableRva = dict_dataDir[dataName[1]].Rva
    offset = get_offset(sectionList, importTableRva)
    raw = get_rawoffset(importTableRva, offset)
    importTableList = get_IID(raw, offset)
    for table in importTableList:
        table.functionList = get_function_list(peFile, table.OriginalFirstThunk, offset)
    # -输出表
    exportTableRva = dict_dataDir[dataName[0]].Rva
    flag = False
    if int(exportTableRva, 16) != 0:
        flag = True
        offset = get_offset(sectionList, exportTableRva)
        raw = get_rawoffset(exportTableRva, offset)
        exportTable = ImageExportTable(peFile, int(raw, 16), int(offset, 16))

    # -资源表
    resourceTableRva = dict_dataDir[dataName[2]].Rva
    offset = get_offset(sectionList, resourceTableRva)
    raw = get_rawoffset(resourceTableRva, offset)
    resourceTable = ResourceNode(peFile, int(raw, 16), int(raw, 16))
    resourceTable.get_next_node()
    fp = open('peInformation.txt', 'w')
    #输出
    fp.write("====================IMAGE_DOS_HEADER===================")
    for key, value in dict_dosHeader.items():
        print(key, value, sep=':')
    print("====================IMAGE_NT_HEADER====================")
    print("=============IMAGE_FILE_HEADER=============")
    for key, value in dict_fileHeader.items():
        print(key, value, sep=':')
    print("=========IMAGE_FILE_OPTIONAL_HEADER========")
    for key, value in tmpdict.items():
        print(key, value, sep=':')
    print("===================IMAGE_SECTION_HEADER==================")
    for i in sectionList:
        print(i)
    print("=======================IMPORT_TABLE======================")
    for table in importTableList:
        print(table)
        print("function list:")
        for func in table.functionList:
            print("hint:" + func.hint + " name:" + func.name)
    print('=======================IMPORT_TABLE======================')
    print('Characteristics:' + exportTable.Characteristics)
    print('TimeDateStamp:' + exportTable.TimeDateStamp)
    print('MinorVersion:'+exportTable.MinorVersion)
    print('MinorVersion:'+exportTable.MinorVersion)
    print('Name:'+exportTable.Name)
    print('Base:'+exportTable.Base)
    print('NumberOfFunctions:'+exportTable.NumberOfFunctions)
    print('NumberOfNames:'+exportTable.NumberOfNames)
    print('AddressOfFunctions:'+exportTable.AddressOfFunctions)
    print('AddressOfNames:'+exportTable.AddressOfNames)
    print('AddressOfNameOrdinals:'+exportTable.AddressOfNameOrdinals)
    print('Export Functions Information:')
    total = int(exportTable.NumberOfFunctions, 16)
    print('total: %d' % total)
    for i in range(total):
        tmp = int(exportTable.NameOrdinals[i], 16)
        print('Name:{0} | ord:{1} | rva:{2}'.format(exportTable.Names[i], tmp, exportTable.Addresses[tmp]))
    print("======================RESOURCE_TABLE=====================")
    print(resourceTable)
    for i in resourceTable.entries:
        print(i)
        print('----', i.nextnode)
        i.nextnode.get_next_node()
        for j in i.nextnode.entries:
            print('----', j)
            print('--------', j.nextnode)
            j.nextnode.get_next_node()
            for k in j.nextnode.entries:
                print('--------', k)
                print('------------', k.dataEntry, '\n')


    #文件版本
    # fp.write("====================IMAGE_DOS_HEADER===================\n")
    # for key, value in dict_dosHeader.items():
    #     fp.write(key+':'+value+'\n')
    # fp.write("====================IMAGE_NT_HEADER====================\n")
    # fp.write("=============IMAGE_FILE_HEADER=============\n")
    # for key, value in dict_fileHeader.items():
    #     fp.write(key+':'+value+'\n')
    # fp.write("=========IMAGE_FILE_OPTIONAL_HEADER========\n")
    # for key, value in dict_fileOptionalHeader.items():
    #     fp.write(key+':'+value+'\n')
    # fp.write("===================IMAGE_SECTION_HEADER==================\n")
    # for i in sectionList:
    #     fp.write(i.__str__()+'\n')
    # fp.write("=======================IMPORT_TABLE======================\n")
    # for table in importTableList:
    #     fp.write('\n'+table.__str__())
    #     fp.write("function list:\n")
    #     for func in table.functionList:
    #         fp.write("hint:" + func.hint + " name:" + func.name+'\n')
    # if flag:
    #     fp.write('=======================EXPORT_TABLE======================\n')
    #     fp.write('Characteristics:' + exportTable.Characteristics+'\n')
    #     fp.write('TimeDateStamp:' + exportTable.TimeDateStamp+'\n')
    #     fp.write('MinorVersion:' + exportTable.MinorVersion+'\n')
    #     fp.write('MinorVersion:' + exportTable.MinorVersion+'\n')
    #     fp.write('Name:' + exportTable.Name+'\n')
    #     fp.write('Base:' + exportTable.Base+'\n')
    #     fp.write('NumberOfFunctions:' + exportTable.NumberOfFunctions+'\n')
    #     fp.write('NumberOfNames:' + exportTable.NumberOfNames+'\n')
    #     fp.write('AddressOfFunctions:' + exportTable.AddressOfFunctions+'\n')
    #     fp.write('AddressOfNames:' + exportTable.AddressOfNames+'\n')
    #     fp.write('AddressOfNameOrdinals:' + exportTable.AddressOfNameOrdinals+'\n')
    #     fp.write('Export Functions Information:'+'\n')
    #     total = int(exportTable.NumberOfFunctions, 16)
    #     fp.write('total:'+str(total) + '\n')
    #     for i in range(total):
    #         tmp = int(exportTable.NameOrdinals[i], 16)
    #         fp.write('Name:{0} | ord:{1} | rva:{2}\n'.format(exportTable.Names[i], tmp, exportTable.Addresses[tmp]))
    # fp.write("======================RESOURCE_TABLE=====================\n")
    # fp.write(resourceTable.__str__()+'\n')
    # for i in resourceTable.entries:
    #     fp.write(i.__str__()+'\n')
    #     fp.write('----'+i.nextnode.__str__()+'\n')
    #     i.nextnode.get_next_node()
    #     for j in i.nextnode.entries:
    #         fp.write('----' + j.__str__() + '\n')
    #         fp.write('--------' + j.nextnode.__str__() + '\n')
    #         j.nextnode.get_next_node()
    #         for k in j.nextnode.entries:
    #             fp.write('--------'+k.__str__()+'\n')
    #             fp.write('------------'+k.dataEntry.__str__()+'\n')
