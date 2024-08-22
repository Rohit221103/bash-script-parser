CASE1=1 CASE2=4.5  #variable declaration
echo $CASE1,$CASE2
# ignore comment
Fruits=('Apple' 'Banana' 'Orange') #array declaration
Fruits[0]="Apple"
Fruits[1]="Banana"
Fruits[2]="Orange"
echo "${Fruits[0]}"           
if (( $CASE1 <= 2 )); then   #conditional
	echo "correct"
fi
for i in "${arrayName[@]}"; do #iteration
  echo "$i"
done
myfunc() {                  # function definition
    echo "hello $1"
}
myfunc "John"
