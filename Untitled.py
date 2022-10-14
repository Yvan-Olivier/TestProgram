{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "46613cad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[20, 30, 40]\n"
     ]
    }
   ],
   "source": [
    "nbre_ligne, nbre_col = input().split()\n",
    "nbre_ligne = int(nbre_lignes)\n",
    "nbre_col = int(nbre_col)\n",
    "code = []\n",
    "\n",
    "for i in range(nbre_ligne):\n",
    "    ligne = list(input())\n",
    "    code.append(ligne)\n",
    "\n",
    "norme_ligne = []\n",
    "norme_col = []\n",
    "\n",
    "ligne = input()\n",
    "col = input()\n",
    "for i in ligne.split():\n",
    "    norme_ligne.append(int(i))\n",
    "for j in col.split()\n",
    "    norme_col.append(int(j))\n",
    "    \n",
    "# Verifications de la conformité\n",
    "\n",
    "\n",
    "\n",
    "        \n",
    "        \n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "d8756673",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'b', 'c', 'd']"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ls = 'abcd'\n",
    "ls = list(ls)\n",
    "ls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "376fa6bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "4 3 2 1\n",
      "8\n",
      "1 2 3 4 5 6 7 8 \n",
      "POSSIBLE\n"
     ]
    }
   ],
   "source": [
    "nbre_rangee = int(input())\n",
    "nbre_place = list(input().split())\n",
    "nbre_pers = int(input())\n",
    "niveau = list(input().split())\n",
    "bool = True\n",
    "\n",
    "for i in range(len(nbre_place)):\n",
    "    nbre_place[i] = int(nbre_place[i])\n",
    "for i in range(len(niveau)):\n",
    "   niveau[i] = int(niveau[i])\n",
    "    \n",
    "niveau.sort()\n",
    "\n",
    "if nbre_pers > sum(nbre_place) : \n",
    "    bool = False\n",
    "    print(\"IMPOSSIBLE\")\n",
    "    exit();\n",
    " \n",
    "for rang,place in enumerate(nbre_place):\n",
    "    if len(niveau) >= place:\n",
    "        for i in range (place) :\n",
    "            if niveau[i] < rang+1 :\n",
    "                bool = False\n",
    "                print(\"IMPOSSIBLE\")\n",
    "                break;\n",
    "        niveau = niveau[place:]\n",
    "        \n",
    "    else:\n",
    "        for i in range (len(niveau)) :\n",
    "            if niveau[i] < rang+1 :\n",
    "                bool = False\n",
    "                print(\"IMPOSSIBLE\")\n",
    "                break;\n",
    "\n",
    "if bool :\n",
    "    print(\"POSSIBLE\")\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6e17b1e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/1w/2hf8k1tn0454zj3_2tkj_cqm0000gn/T/ipykernel_38569/2057360503.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0ml\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m5\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ml\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ml\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "04a57f59",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 5\n",
      "2\n",
      "3\n",
      "55\n"
     ]
    }
   ],
   "source": [
    "Xm,Xr = input().split()\n",
    "Xm = int(Xm)\n",
    "Xr = int(Xr)\n",
    "N = int(input())\n",
    "transport = []\n",
    "couleur = []\n",
    "nombre = []\n",
    "\n",
    "for i in range(N):\n",
    "    t, c, nbre = input().split()\n",
    "    if t = 'v':\n",
    "        transport.append(t)\n",
    "        couleur.append(c)\n",
    "        nombre.append(int(nbre))\n",
    "    else :\n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "dadbdf26",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "50 10\n",
      "3\n",
      "v m 4\n",
      "v r 2\n",
      "b 15\n",
      "-18 6 15\n"
     ]
    }
   ],
   "source": [
    "Xm,Xr = input().split()\n",
    "Xm = int(Xm)\n",
    "Xr = int(Xr)\n",
    "N = int(input())\n",
    "nbre_voiture = 0\n",
    "nbre_bus = 0\n",
    "pas_transport = Xm\n",
    "\n",
    "for i in range(N):\n",
    "    enter = list(input().split())\n",
    "    if enter[0] == 'v' :\n",
    "        nbre_voiture = nbre_voiture + int(enter[2])\n",
    "        pas_transport = pas_transport - int(enter[2])\n",
    "    else :\n",
    "        nbre_bus = nbre_bus + int(enter[1])\n",
    "        pas_transport = pas_transport - int(enter[1])\n",
    "\n",
    "print(pas_transport, nbre_voiture, nbre_bus)\n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8777be5d",
   "metadata": {},
   "outputs": [],
   "source": [
    "L, nbre_grp = input()\n",
    "L = int(L)\n",
    "nbre_grp = int(nbre_grp)\n",
    "grp = []\n",
    "for i in range (nbre_grp):\n",
    "    grp.append(int(input()))\n",
    "\n",
    "for i in range (nbre_grp-1) :\n",
    "    for j in range (i+1, nbre_grp):\n",
    "        \n",
    "    \n",
    "        \n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
