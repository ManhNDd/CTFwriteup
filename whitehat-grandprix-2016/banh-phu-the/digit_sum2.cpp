#include <unordered_map>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <inttypes.h>

using namespace std;

unordered_map<int64_t, int64_t> mDict;


int64_t nDiv2(int64_t n) {
	if (n % 2 == 1) return nDiv2(n-1);
	return n/2+1;
}

string numberToString(int64_t n) // OK
{
	char buf1[21];
	char buf2[21];
	memset(buf1, 0, sizeof(buf1));
	memset(buf2, 0, sizeof(buf2));
	
	int i = 0;
	buf1[i] = (n % 10) + '0';
	n = n / 10;
	while(n != 0) {
		++i;
		buf1[i] = (n % 10) + '0';
		n = n / 10;
	}
	
	int len = strlen(buf1);
	for(int j = len-1; j >= 0; --j) buf2[len-1-j] = buf1[j];
	return string(buf2);
}

int64_t stringToNumber(const string& strN) // OK
{
	
	int64_t n = strN[0]-'0';
	int i = 1;
	for(; i < strN.length(); ++i) {
		n = n*10+(strN[i]-'0');
	}
	return n;
}
	
int64_t smallPower(int base, int pow) // OK
{
	int64_t ret = 1;
	for(int i = 0; i < pow; ++i) ret *= base;
	return ret;
}
	
int64_t digitSum(int64_t n)
{
	if (mDict.find(n) != mDict.end()) return mDict[n];
	string strN = numberToString(n);
	if (strN.length() < 2) {
		if (n % 2 == 1) n = n-1;
		return n*nDiv2(n)/2;
	}
	int64_t tmp999 = smallPower(10, strN.length()-1) - 1;
	int64_t a = strN[0] - '0';
	int64_t bcd = stringToNumber(strN.substr(1));
	int64_t ret = a*(a-1)/2*nDiv2(tmp999) + a*digitSum(tmp999) + a*nDiv2(bcd) + digitSum(bcd);
	mDict[n] = ret;
	return ret;
}
/*
thoi gian doc vao ra khong anh huong, do ta dung cpu time
*/
int main(int argc, char** argv)
{	
	int fscanf(FILE *stream, const char *format, ...);
	FILE* ifile = fopen(argv[1], "r");
	FILE* ofile = fopen(argv[2], "w");
	int T;
	fscanf(ifile, "%d", &T);
	for(int i = 0; i < T; ++i) {
		int64_t N1, N2;
		fscanf(ifile, "%" PRId64, &N1);
		fscanf(ifile, "%" PRId64, &N2);
		if (N1 == 0) {
			fprintf(ofile, "%" PRId64 "\n", digitSum(N2));
		} else {
			fprintf(ofile, "%" PRId64 "\n", (digitSum(N2) - digitSum(N1-1)));
		}
	}
	return 0;
}
.