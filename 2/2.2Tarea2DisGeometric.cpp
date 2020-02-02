/* This program performs a script to plot a discrete geometric distribution

   The file dis-geometric.gnu is generated. You need to install gnuplot 
   in order to plot this data with the shell command gnuplot dis-geometric.gnu. 
   It will be generated the file dis-geometric.png.

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
    string sp;
    cout << "p = ";
    cin >> sp;
    
    double p;

    try
    {
        p = stod(sp, nullptr);   
    }
    catch(const exception & e)
    {
        cout << "error: invalid input" << '\n';
        return 0;
    }
    
    ofstream file("dis-geometric.gnu");

    file    << "set term png\n"
            << "set output \'dis-geometric.png\'\n"
            << "# Geometric PDF\n"
            << "isint(x)=(int(x)==x)\n"
            << "geometric(x,p)=p<=0||p>1?1/0:  !isint(x)?1/0:x<0||p==1?(x==0?1.0:0.0):exp(log(p)+x*log(1.0-p))\n"
            << "p = " << p << "\n"
            << "mu = (1.0 - p) / p\n"
            << "sigma = sqrt(mu / p)\n"
            << "xmin = int(mu - 4.0 * sigma)\n"
            << "xmin = xmin < -1 ? -1 : xmin\n"
            << "xmin = -1\n"
            << "xmax = int(mu + 4.0 * sigma)\n"
            << "ymax = 1.1 * geometric(0, p) #mode of geometric PDF used\n"
            << "unset key\n"
            << "unset zeroaxis\n"
            << "set xrange [xmin : xmax]\n"
            << "set yrange [0 : ymax]\n"
            << "set xlabel \"k ->\"\n"
            << "set ylabel \"probability density ->\"\n"
            << "set ytics 0, ymax / 10, ymax\n"
            << "set format x \"%2.0f\"\n"
            << "set format y \"%3.2f\"\n"
            << "set sample (xmax - xmin) + 1\n"
            << "set title \"geometric PDF with p = " << p << "\"\n"
            << "plot geometric(x, p) with impulses\n";

    file.close();
}
