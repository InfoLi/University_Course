#include<iostream>
#include<fstream>

using namespace std;

//扩展bits
//将二进制数字传入（以字符串形式） --> 拓展成n*512bits
string expand_bits(string bits_contents,string sizeOF_con) {

	const int con_length = bits_contents.length();//获取二进制长度
	int mod = con_length % 512;

	//将bits拓展到n*512
	bits_contents += "1";
	for (int i = 1; i < 448- mod; i++) {
		bits_contents += "0";
	}

	bits_contents += sizeOF_con;//最终处理结果

	return bits_contents;
}


//字符串转化 32位二进制 最大不超过int
int string_to_uint(string num) {
	int number = 0;
	int temp;

	for (int i = 0; i < 32; i++) {
		if (num[i] == '1') {
			number += pow(2, 31 - i);
		}
	}
	return number;
}

//右移 32bits大小的块 √
string rightshift(string str,int num) {
	//binary 是需要右移的字符串
	string ret = "";
	for (int i = 0; i < num; i++) {
		ret += "0";
	}
	for (int i = 31 - num; i>=0 ; i--) {
		ret += str[i];
	}
	return ret;
}

//循环右移函数 √
string rightrotate(string str, int num) {
	string ret = "";
	for (int i = 0; i < num; i++) {
		ret += str[32 - num + i];
	}
	for (int i = 0; i < 32 - num; i++) {
		ret += str[i];
	}

	return ret;
}

//字符串形式的异或 √
string new_xor(string binary_one,string binary_two) {
	string ret = "";
	for (int i = 0; i < 32; i++) {
		if (binary_one[i] == binary_two[i])ret += "0";
		else ret += "1";
	}
	return ret;
}

//字符串形式的补 √
string new_complement(string str) {
	string ret = "";
	for (int i = 0; i < 32; i++) {
		if (str[i] == '1')ret += "0";
		else ret += "1";
	}
	return ret;
}

//字符串形式的与 √
string new_and(string str1, string str2) {
	string ret = "";
	for (int i = 0; i < 32; i++) {
		if ((str1[i] == '1') && (str2[i] == '1'))ret += "1";
		else ret += "0";
	}
	return ret;
}

//二进制相加 需要求余
string add(string str1, string str2) {

	string ret = "";
	//超过即舍弃
	int boo = 0;//进位计量
	for (int i = 31; i >= 0; i--) {
		//需要进位
		if (boo == 1) {
			if ((str1[i] == '1') && (str2[i] == '1')) {
				boo = 1;
				ret += "1";
			}
			else if ((str1[i] == '0') && (str2[i] == '0')) {
				boo = 0;
				ret += "1";
			}
			else {
				boo = 1;
				ret += "0";
			}
		}
		//不需要进位
		else {
			if ((str1[i] == '1') && (str2[i] == '1')) {
				boo = 1;
				ret += "0";
			}
			else if ((str1[i] == '0') && (str2[i] == '0')) {
				boo = 0;
				ret += "0";
			}
			else {
				boo = 0;
				ret += "1";
			}
		}
	}

	//需要翻转一下
	reverse(ret.begin(), ret.end());

	return ret;
}

string Ch(string E, string F, string G) {
	string ret;
	ret = new_xor(new_and(E, F), new_and(new_complement(E), G));
	return ret;
}

string Ma(string A, string B, string C) {
	string ret;
	ret = new_xor(new_xor(new_and(A, B), new_and(A, C)), new_and(B, C));
	return ret;
}

string _A(string A) {
	string ret;

	ret = new_xor(new_xor(rightrotate(A, 2), rightrotate(A, 13)), rightrotate(A, 22));

	return ret;
}

string _E(string E) {
	string ret;

	ret = new_xor(new_xor(rightrotate(E, 6), rightrotate(E, 11)), rightrotate(E, 25));
	
	return ret;
}

string He_to_Bi(string str) {
	string ret = "";
	for (int i = 0; i < 8; i++) {
		switch (str[i])
		{
		case '0':ret += "0000"; break;
		case '1':ret += "0001"; break;
		case '2':ret += "0010"; break;
		case '3':ret += "0011"; break;
		case '4':ret += "0100"; break;
		case '5':ret += "0101"; break;
		case '6':ret += "0110"; break;
		case '7':ret += "0111"; break;
		case '8':ret += "1000"; break;
		case '9':ret += "1001"; break;
		case 'a':ret += "1010"; break;
		case 'b':ret += "1011"; break;
		case 'c':ret += "1100"; break;
		case 'd':ret += "1101"; break;
		case 'e':ret += "1110"; break;
		case 'f':ret += "1111"; break;
		default:
			break;
		}
	}
	return ret;
}

void He_to_Bi_more(string str[64]) {
	string ret = "";

	for (int j = 0; j < 64; j++) {
		ret = "";
		for (int i = 0; i < 8; i++) {
			switch (str[j][i])
			{
			case '0':ret += "0000"; break;
			case '1':ret += "0001"; break;
			case '2':ret += "0010"; break;
			case '3':ret += "0011"; break;
			case '4':ret += "0100"; break;
			case '5':ret += "0101"; break;
			case '6':ret += "0110"; break;
			case '7':ret += "0111"; break;
			case '8':ret += "1000"; break;
			case '9':ret += "1001"; break;
			case 'a':ret += "1010"; break;
			case 'b':ret += "1011"; break;
			case 'c':ret += "1100"; break;
			case 'd':ret += "1101"; break;
			case 'e':ret += "1110"; break;
			case 'f':ret += "1111"; break;
			default:
				break;
			}
		}
		str[j] = ret;
	}
}

void get_hash(string statistic,string result[8]) {
	//8个常量	
	string A = He_to_Bi("6a09e667");
	string B = He_to_Bi("bb67ae85");
	string C = He_to_Bi("3c6ef372");
	string D = He_to_Bi("a54ff53a");
	string E = He_to_Bi("510e527f");
	string F = He_to_Bi("9b05688c");
	string G = He_to_Bi("1f83d9ab");
	string H = He_to_Bi("5be0cd19");
	string temp_A;//处理承接A
	string temp_D;

	string K[64] = { "428a2f98","71374491","b5c0fbcf","e9b5dba5",
					"3956c25b","59f111f1","923f82a4","ab1c5ed5",
					"d807aa98","12835b01","243185be","550c7dc3",
					"72be5d74","80deb1fe","9bdc06a7","c19bf174",
					"e49b69c1","efbe4786","0fc19dc6","240ca1cc",
					"2de92c6f","4a7484aa","5cb0a9dc","76f988da",
					"983e5152","a831c66d","b00327c8","bf597fc7",
					"c6e00bf3","d5a79147","06ca6351","14292967",
					"27b70a85","2e1b2138","4d2c6dfc","53380d13",
					"650a7354","766a0abb","81c2c92e","92722c85",
					"a2bfe8a1","a81a664b","c24b8b70","c76c51a3",
					"d192e819","d6990624","f40e3585","106aa070",
					"19a4c116","1e376c08","2748774c","34b0bcb5",
					"391c0cb3","4ed8aa4a","5b9cca4f","682e6ff3",
					"748f82ee","78a5636f","84c87814","8cc70208",
					"90befffa","a4506ceb","bef9a3f7","c67178f2" };

	He_to_Bi_more(K);//处理得出64个二进制数

	int n = statistic.length() / 512;//获取区块数

	string temp;//储存512bits
	string block;
	string cul_hash[64];

	string s0, s1;//拓展时使用的间接
	int i, j;
	//进行循环得到hash值
	for (int location = 0; location < n; location++) {

		//每次读取512bits
		temp = "";//清空temp
		//得到512bits
		for (i = location*512; i < (location + 1) * 512; i++) {
			temp += statistic[i];
		}

		//处理前16个块
		for (j = 0; j < 16; j++) {
			block = "";//清空block
			for (i = j * 32; i < (j + 1) * 32; i++) {
				block += temp[i];
			}
			cul_hash[j] = block;
		}
		
		//循环得到16-63个块
		for (j = 16; j < 64; j++) {
			s0 = new_xor(new_xor(rightrotate(cul_hash[j - 15], 7), rightrotate(cul_hash[j - 15], 18)), rightshift(cul_hash[j - 15], 3));
			s1 = new_xor(new_xor(rightrotate(cul_hash[j - 2], 17), rightrotate(cul_hash[j - 2], 19)), rightshift(cul_hash[j - 10], 3));

			cul_hash[j] = add(add(add(cul_hash[j - 16], s0), cul_hash[j - 7]), s1);//怎么处理溢出呢？
		}

		//64次循环处理得到新一轮的hash值
		for (int k = 0; k < 64; k++) {
			temp_A = add(cul_hash[k], K[k]);
			temp_A = add(add(Ch(E, F, G), H), temp_A);
			temp_A = add(_E(E), temp_A);

			temp_D = add(D, temp_A);

			temp_A = add(Ma(A, B, C), temp_A);
			temp_A = add(_A(A), temp_A);

			//更新hash值
			H = G;
			G = F;
			F = E;
			E = temp_D;
			D = C;
			C = B;
			B = A;
			A = temp_A;
		}
	}
	result[0] = A; result[1] = B; result[2] = C; result[3] = D; result[4] = E; result[5] = F; result[6] = G; result[7] = H;
}

void cc(string str[8]) {
	//8*32
	string ret = "";
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 32; j++) {
			if ((j+1) % 4 == 0) {
				ret += str[i][j];
				if (ret == "0000") cout << '0';
				else if (ret == "0001") cout << '1';
				else if (ret == "0010") cout << '2';
				else if (ret == "0011") cout << '3';
				else if (ret == "0100") cout << '4';
				else if (ret == "0101") cout << '5';
				else if (ret == "0110") cout << '6';
				else if (ret == "0111") cout << '7';
				else if (ret == "1000") cout << '8';
				else if (ret == "0001") cout << '9';
				else if (ret == "1010") cout << 'a';
				else if (ret == "1011") cout << 'b';
				else if (ret == "1100") cout << 'c';
				else if (ret == "1101") cout << 'd';
				else if (ret == "1110") cout << 'e';
				else if (ret == "1111") cout << 'f';
				ret = "";
			}
			else {
				ret += str[i][j];
			}
		}
	}
}

int main() {
	
	string result[8];
	string bits_contents, sizeOF_con;
	bits_contents = "000000000110000100000000011000100000000001100011";

	sizeOF_con = "00000000\
00000000\
00000000\
00000000\
00000000\
00000000\
00000000\
00011000";
	 get_hash(expand_bits(bits_contents, sizeOF_con), result);

	 cc(result);

	return 0;
}

