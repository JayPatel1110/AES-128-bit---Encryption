# AES-128-bit---Encryption
Software Implementation of the encryption algorithm using python 2.7.12
This repository includes my project work with every module implementation seperately with final and modified version of the AES encryption.
Description about all code files as below:
1. Project 2_JMD_KS - The file contains the code for the step called Key Schedule of AES.
                      Input - 32 hex numbers (128 bit) i.e. 000102030405060708090a0b0c0d0e0f
                      Output - 11 python list for Round 0 to 10 each has 32 hex numbers (128 bit)
                               Round 0 :
                               Key: ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f']
                               Round 1 :
                               Key: ['d6', 'aa', '74', 'fd', 'd2', 'af', '72', 'fa', 'da', 'a6', '78', 'f1', 'd6', 'ab', '76', 'fe']
                               Round 2 :
                               Key: ['b6', '92', 'cf', '0b', '64', '3d', 'bd', 'f1', 'be', '9b', 'c5', '00', '68', '30', 'b3', 'fe']
                               Round 3 :
                               Key: ['b6', 'ff', '74', '4e', 'd2', 'c2', 'c9', 'bf', '6c', '59', '0c', 'bf', '04', '69', 'bf', '41']
                               Round 4 :
                               Key: ['47', 'f7', 'f7', 'bc', '95', '35', '3e', '03', 'f9', '6c', '32', 'bc', 'fd', '05', '8d', 'fd']
                               Round 5 :
                               Key: ['3c', 'aa', 'a3', 'e8', 'a9', '9f', '9d', 'eb', '50', 'f3', 'af', '57', 'ad', 'f6', '22', 'aa'] 
                               Round 6 :
                               Key: ['5e', '39', '0f', '7d', 'f7', 'a6', '92', '96', 'a7', '55', '3d', 'c1', '0a', 'a3', '1f', '6b'] 
                               Round 7 :
                               Key: ['14', 'f9', '70', '1a', 'e3', '5f', 'e2', '8c', '44', '0a', 'df', '4d', '4e', 'a9', 'c0', '26'] 
                               Round 8 :
                               Key: ['47', '43', '87', '35', 'a4', '1c', '65', 'b9', 'e0', '16', 'ba', 'f4', 'ae', 'bf', '7a', 'd2'] 
                               Round 9 :
                               Key: ['54', '99', '32', 'd1', 'f0', '85', '57', '68', '10', '93', 'ed', '9c', 'be', '2c', '97', '4e'] 
                               Round 10 :
                               Key: ['13', '11', '1d', '7f', 'e3', '94', '4a', '17', 'f3', '07', 'a7', '8b', '4d', '2b', '30', 'c5']

2. Project 2_JMD_ARK - This file includes the python implementation of Add-Round key step of AES encryption.
                       Input - 32 hex numbers (128 bit) for both data and key input
                               i.e. data: 00112233445566778899aabbccddeeff
                                     key: 000102030405060708090a0b0c0d0e0f
                       Output - python list of 32 hex numbers (128 bit) 
                                i.e. ['00', '10', '20', '30', '40', '50', '60', '70', '80', '90', 'a0', 'b0', 'c0', 'd0', 'e0', 'f0']

3. Project 2_JMD_BS - This file contains code for Byte-substitution step of AES Implementation.
                      Input - 32 hex numbers (128 bit) i.e. 00102030405060708090a0b0c0d0e0f0
                      Output - python list of 32 hex numbers (128 bit)
                               i.e.  ['63', 'ca', 'b7', '04', '09', '53', 'd0', '51', 'cd', '60', 'e0', 'e7', 'ba', '70', 'e1', '8c']

4. Project 2_JMD_SR - It is the code for Shift-Row step of AES.
                      Input - 32 hex numbers (128 bit) i.e. 63cab7040953d051cd60e0e7ba70e18c
                      Output - python list of 32 hex numbers (128 bit) 
                               i.e. ['63', '53', 'e0', '8c', '09', '60', 'e1', '04', 'cd', '70', 'b7', '51', 'ba', 'ca', 'd0', 'e7']

5. Project 2_JMD_MC - .py file includes the code for Mix-Column step of python implementation.
                      Input - 32 hex numbers (128 bit) i.e. 6353e08c0960e104cd70b751bacad0e7
                      Output - python list of 32 hex numbers (128 bit)
                               i.e. ['5f', '72', '64', '15', '57', 'f5', 'bc', '92', 'f7', 'be', '3b', '29', '1d', 'b9', 'f9', '1a']
6. Project 2_JMD_Final_modified AES - The code is for modified implementation of AES, where The the row number 4 and 5 of SBox were interchanged.

7. Project 2_JMD_Final - The code is dedicated for original AES implementation. Sample output is given as below.
===========================================================================================================
Advance Security Encryption programmed in Python(2.7.12) by "Savan Darji(M.Eng Student)@Uwindsor"
===========================================================================================================
Enter the data:00112233445566778899aabbccddeeff
Enter the key:000102030405060708090a0b0c0d0e0f
Original Plaintext and Key:
Input: 00112233445566778899aabbccddeeff
Key:   000102030405060708090a0b0c0d0e0f
==========================================================================================================
Key Schedule Results for Each Round:
==========================================================================================================
Round 0 :
     Key: ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f'] 

Round 1 :
     Key: ['d6', 'aa', '74', 'fd', 'd2', 'af', '72', 'fa', 'da', 'a6', '78', 'f1', 'd6', 'ab', '76', 'fe'] 

Round 2 :
     Key: ['b6', '92', 'cf', '0b', '64', '3d', 'bd', 'f1', 'be', '9b', 'c5', '00', '68', '30', 'b3', 'fe'] 

Round 3 :
     Key: ['b6', 'ff', '74', '4e', 'd2', 'c2', 'c9', 'bf', '6c', '59', '0c', 'bf', '04', '69', 'bf', '41'] 

Round 4 :
     Key: ['47', 'f7', 'f7', 'bc', '95', '35', '3e', '03', 'f9', '6c', '32', 'bc', 'fd', '05', '8d', 'fd'] 

Round 5 :
     Key: ['3c', 'aa', 'a3', 'e8', 'a9', '9f', '9d', 'eb', '50', 'f3', 'af', '57', 'ad', 'f6', '22', 'aa'] 

Round 6 :
     Key: ['5e', '39', '0f', '7d', 'f7', 'a6', '92', '96', 'a7', '55', '3d', 'c1', '0a', 'a3', '1f', '6b'] 

Round 7 :
     Key: ['14', 'f9', '70', '1a', 'e3', '5f', 'e2', '8c', '44', '0a', 'df', '4d', '4e', 'a9', 'c0', '26'] 

Round 8 :
     Key: ['47', '43', '87', '35', 'a4', '1c', '65', 'b9', 'e0', '16', 'ba', 'f4', 'ae', 'bf', '7a', 'd2'] 

Round 9 :
     Key: ['54', '99', '32', 'd1', 'f0', '85', '57', '68', '10', '93', 'ed', '9c', 'be', '2c', '97', '4e'] 

Round 10 :
     Key: ['13', '11', '1d', '7f', 'e3', '94', '4a', '17', 'f3', '07', 'a7', '8b', '4d', '2b', '30', 'c5'] 

===========================================================================================================
Intermediate Results at Each Round:
===========================================================================================================
Round 0 : 
----Start: ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']
---Output: ['00', '10', '20', '30', '40', '50', '60', '70', '80', '90', 'a0', 'b0', 'c0', 'd0', 'e0', 'f0'] 

Round 1 :
----Start: ['00', '10', '20', '30', '40', '50', '60', '70', '80', '90', 'a0', 'b0', 'c0', 'd0', 'e0', 'f0']
-----SBox: ['63', 'ca', 'b7', '04', '09', '53', 'd0', '51', 'cd', '60', 'e0', 'e7', 'ba', '70', 'e1', '8c']
-ShiftRow: ['63', '53', 'e0', '8c', '09', '60', 'e1', '04', 'cd', '70', 'b7', '51', 'ba', 'ca', 'd0', 'e7']
MixColumn: ['5f', '72', '64', '15', '57', 'f5', 'bc', '92', 'f7', 'be', '3b', '29', '1d', 'b9', 'f9', '1a']
---Output: ['89', 'd8', '10', 'e8', '85', '5a', 'ce', '68', '2d', '18', '43', 'd8', 'cb', '12', '8f', 'e4'] 

Round 2 :
----Start: ['89', 'd8', '10', 'e8', '85', '5a', 'ce', '68', '2d', '18', '43', 'd8', 'cb', '12', '8f', 'e4']
-----SBox: ['a7', '61', 'ca', '9b', '97', 'be', '8b', '45', 'd8', 'ad', '1a', '61', '1f', 'c9', '73', '69']
-ShiftRow: ['a7', 'be', '1a', '69', '97', 'ad', '73', '9b', 'd8', 'c9', 'ca', '45', '1f', '61', '8b', '61']
MixColumn: ['ff', '87', '96', '84', '31', 'd8', '6a', '51', '64', '51', '51', 'fa', '77', '3a', 'd0', '09']
---Output: ['49', '15', '59', '8f', '55', 'e5', 'd7', 'a0', 'da', 'ca', '94', 'fa', '1f', '0a', '63', 'f7'] 

Round 3 :
----Start: ['49', '15', '59', '8f', '55', 'e5', 'd7', 'a0', 'da', 'ca', '94', 'fa', '1f', '0a', '63', 'f7']
-----SBox: ['3b', '59', 'cb', '73', 'fc', 'd9', '0e', 'e0', '57', '74', '22', '2d', 'c0', '67', 'fb', '68']
-ShiftRow: ['3b', 'd9', '22', '68', 'fc', '74', 'fb', '73', '57', '67', 'cb', 'e0', 'c0', '59', '0e', '2d']
MixColumn: ['4c', '9c', '1e', '66', 'f7', '71', 'f0', '76', '2c', '3f', '86', '8e', '53', '4d', 'f2', '56']
---Output: ['fa', '63', '6a', '28', '25', 'b3', '39', 'c9', '40', '66', '8a', '31', '57', '24', '4d', '17'] 

Round 4 :
----Start: ['fa', '63', '6a', '28', '25', 'b3', '39', 'c9', '40', '66', '8a', '31', '57', '24', '4d', '17']
-----SBox: ['2d', 'fb', '02', '34', '3f', '6d', '12', 'dd', '09', '33', '7e', 'c7', '5b', '36', 'e3', 'f0']
-ShiftRow: ['2d', '6d', '7e', 'f0', '3f', '33', 'e3', '34', '09', '36', '02', 'dd', '5b', 'fb', '12', 'c7']
MixColumn: ['63', '85', 'b7', '9f', 'fc', '53', '8d', 'f9', '97', 'be', '47', '8e', '75', '47', 'd6', '91']
---Output: ['24', '72', '40', '23', '69', '66', 'b3', 'fa', '6e', 'd2', '75', '32', '88', '42', '5b', '6c'] 

Round 5 :
----Start: ['24', '72', '40', '23', '69', '66', 'b3', 'fa', '6e', 'd2', '75', '32', '88', '42', '5b', '6c']
-----SBox: ['36', '40', '09', '26', 'f9', '33', '6d', '2d', '9f', 'b5', '9d', '23', 'c4', '2c', '39', '50']
-ShiftRow: ['36', '33', '9d', '50', 'f9', 'b5', '39', '26', '9f', '2c', '09', '2d', 'c4', '40', '6d', '23']
MixColumn: ['f4', 'bc', 'd4', '54', '32', 'e5', '54', 'd0', '75', 'f1', 'd6', 'c5', '1d', 'd0', '3b', '3c']
---Output: ['c8', '16', '77', 'bc', '9b', '7a', 'c9', '3b', '25', '02', '79', '92', 'b0', '26', '19', '96'] 

Round 6 :
----Start: ['c8', '16', '77', 'bc', '9b', '7a', 'c9', '3b', '25', '02', '79', '92', 'b0', '26', '19', '96']
-----SBox: ['e8', '47', 'f5', '65', '14', 'da', 'dd', 'e2', '3f', '77', 'b6', '4f', 'e7', 'f7', 'd4', '90']
-ShiftRow: ['e8', 'da', 'b6', '90', '14', '77', 'd4', '65', '3f', 'f7', 'f5', 'e2', 'e7', '47', 'dd', '4f']
MixColumn: ['98', '16', 'ee', '74', '00', 'f8', '7f', '55', '6b', '2c', '04', '9c', '8e', '5a', 'd0', '36']
---Output: ['c6', '2f', 'e1', '09', 'f7', '5e', 'ed', 'c3', 'cc', '79', '39', '5d', '84', 'f9', 'cf', '5d'] 

Round 7 :
----Start: ['c6', '2f', 'e1', '09', 'f7', '5e', 'ed', 'c3', 'cc', '79', '39', '5d', '84', 'f9', 'cf', '5d']
-----SBox: ['b4', '15', 'f8', '01', '68', '58', '55', '2e', '4b', 'b6', '12', '4c', '5f', '99', '8a', '4c']
-ShiftRow: ['b4', '58', '12', '4c', '68', 'b6', '8a', '01', '4b', '99', 'f8', '2e', '5f', '15', '55', '4c']
MixColumn: ['c5', '7e', '1c', '15', '9a', '9b', 'd2', '86', 'f0', '5f', '4b', 'e0', '98', 'c6', '34', '39']
---Output: ['d1', '87', '6c', '0f', '79', 'c4', '30', '0a', 'b4', '55', '94', 'ad', 'd6', '6f', 'f4', '1f'] 

Round 8 :
----Start: ['d1', '87', '6c', '0f', '79', 'c4', '30', '0a', 'b4', '55', '94', 'ad', 'd6', '6f', 'f4', '1f']
-----SBox: ['3e', '17', '50', '76', 'b6', '1c', '04', '67', '8d', 'fc', '22', '95', 'f6', 'a8', 'bf', 'c0']
-ShiftRow: ['3e', '1c', '22', 'c0', 'b6', 'fc', 'bf', '76', '8d', 'a8', '50', '67', 'f6', '17', '04', '95']
MixColumn: ['ba', 'a0', '3d', 'e7', 'a1', 'f9', 'b5', '6e', 'd5', '51', '2c', 'ba', '5f', '41', '4d', '23']
---Output: ['fd', 'e3', 'ba', 'd2', '05', 'e5', 'd0', 'd7', '35', '47', '96', '4e', 'f1', 'fe', '37', 'f1'] 

Round 9 :
----Start: ['fd', 'e3', 'ba', 'd2', '05', 'e5', 'd0', 'd7', '35', '47', '96', '4e', 'f1', 'fe', '37', 'f1']
-----SBox: ['54', '11', 'f4', 'b5', '6b', 'd9', '70', '0e', '96', 'a0', '90', '2f', 'a1', 'bb', '9a', 'a1']
-ShiftRow: ['54', 'd9', '90', 'a1', '6b', 'a0', '9a', 'b5', '96', 'bb', 'f4', '0e', 'a1', '11', '70', '2f']
MixColumn: ['e9', 'f7', '4e', 'ec', '02', '30', '20', 'f6', '1b', 'f2', 'cc', 'f2', '35', '3c', '21', 'c7']
---Output: ['bd', '6e', '7c', '3d', 'f2', 'b5', '77', '9e', '0b', '61', '21', '6e', '8b', '10', 'b6', '89'] 

Round 10:
----Start: ['bd', '6e', '7c', '3d', 'f2', 'b5', '77', '9e', '0b', '61', '21', '6e', '8b', '10', 'b6', '89']
-----SBox: ['7a', '9f', '10', '27', '89', 'd5', 'f5', '0b', '2b', 'ef', 'fd', '9f', '3d', 'ca', '4e', 'a7']
-ShiftRow: ['7a', 'd5', 'fd', 'a7', '89', 'ef', '4e', '27', '2b', 'ca', '10', '0b', '3d', '9f', 'f5', '9f']
---Output: ['69', 'c4', 'e0', 'd8', '6a', '7b', '04', '30', 'd8', 'cd', 'b7', '80', '70', 'b4', 'c5', '5a']


Note: All above sample data can be used as a test vector for checking the program.
