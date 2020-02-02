/* This program performs a script to plot a discrete binomial distribution

   The file dis-binomial.gnu is generated. You need to install gnuplot 
   in order to plot this data with the shell command gnuplot dis-binomial.gnu. 
   It will be generated the file dis-binomial.png.

   @author: Diego A. Martinez R
   @date:   2/12/2019
*/

#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[])
{
    string sn, sp;
    cout << "n = ";
    cin >> sn; 
    cout << "p = ";
    cin >> sp;
    
    int n;
    double p;

    try
    {
        n = stoi(sn, nullptr, 10);
        p = stod(sp, nullptr);   
    }
    catch(const exception & e)
    {
        cout << "error: invalid arguments" << '\n';
        return 0;
    }
    
    if (p > 1 or n < 1) {
        cout << "error: invalid arguments" << '\n';
        return 0;
    }

    ofstream file("dis-binomial.gnu");

    file    << "set term png\n"
            << "set output \'dis-binomial.png\'\n"
            << "# Binomial PDF\n"
            << "isint(x)=(int(x)==x)\n"
            << "binom(x,n,p)=p<0.0||p>1.0||n<0||!isint(n)?1/0:  !isint(x)?1/0:x<0||x>n?0.0:exp(lgamma(n+1)-lgamma(n-x+1)-lgamma(x+1)  +x*log(p)+(n-x)*log(1.0-p))\n"
            << "n = " << n << "\n"
            << "p = " << p << "\n" 
            << "mu = n * p\n"
            << "sigma = sqrt(n * p * (1.0 - p))\n"
            << "xmin = int(mu - 4.0 * sigma)\n"
            << "xmin = xmin < -2 ? -2 : xmin\n"
            << "xmax = int(mu + 4.0 * sigma)\n"
            << "xmax = xmax < n+2 ? n+2 : xmax\n"
            << "ymax = 1.1 * binom(int((n+1)*p), n, p) #Mode of binomial PDF used\n"
            << "unset key\n"
            << "unset zeroaxis\n"
            << "set xrange [xmin: xmax]\n"
            << "set yrange [0: ymax]\n"
            << "set xlabel \"x ->\"\n"
            << "set ylabel \"probability density ->\"\n"
            << "set ytics 0, ymax / 10, ymax\n"
            << "set format x \"%2.0f\"\n"
            << "set format y \"%3.2f\"\n"
            << "set sample (xmax - xmin)  + 1\n"
            << "set title \"binomial PDF with n = " << n << ", p = " << p << "\n"
            << "plot binom(x, n, p) with impulses";
    
    file.close();
}