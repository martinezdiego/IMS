LIBS = -I.
FLAGS = -std=c++11

run-dis-uniform: dis-uniform
	./dis-uniform && gnuplot dis-uniform.gnu

dis-uniform: 2.2Tarea2DisUniforme.cpp
	g++ ${LIBS} ${FLAGS} -o $@ $^

run-dis-binomial: dis-binomial 
	./dis-binomial && gnuplot dis-binomial.gnu

dis-binomial: 2.2Tarea2DisBinomial.cpp
	g++ ${LIBS} ${FLAGS} -o $@ $^

run-dis-poisson: dis-poisson
	./dis-poisson && gnuplot dis-poisson.gnu

dis-poisson: 2.2Tarea2DisPoisson.cpp
	g++ ${LIBS} ${FLAGS} -o $@ $^

run-dis-exponential: dis-exponential
	./dis-exponential && gnuplot dis-exponential.gnu

dis-exponential: 2.2Tarea2DisExponential.cpp
	g++ ${LIBS} ${FLAGS} -o $@ $^

run-dis-normal : dis-normal
	./dis-normal && gnuplot dis-normal.gnu

dis-normal: 2.2Tarea2DisNormal.cpp
	g++ ${LIBS} ${FLAGS} -o $@ $^

run-dis-geometric: dis-geometric
	./dis-geometric && gnuplot dis-geometric.gnu

dis-geometric: 2.2Tarea2DisGeometric.cpp
	g++ ${LIBS} ${FLAGS} -o $@ $^

clean:
	$(RM) *.o *.png *.gnu dis-uniform dis-binomial dis-poisson dis-normal dis-exponential dis-geometric