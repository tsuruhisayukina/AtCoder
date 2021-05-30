#! usr/bin/zsh

echo "contest number input"
read number
for i in a b c d e f;
do
  touch ABC$number$i.py
done
