�
    �@d?  �                   �  � d dl Z d dlmZ d dlZd dlZd dlZd� Zd� Zd� Zd� Z	d� Z
d� Zd	� Zd
� Zd� Zd� Zd� Zd� Z e�   �           e�   �           e�   �          	  ed�  �        ZdZ ed�  �        ZdZeek    r ej        d�  �         nodZeD ]EZej        �                    e�  �         ej        �                    �   �           ej        d�  �         �F e j        d�  �          e�   �           e�   �          �� e	�   �           e�   �           e�   �           e
�   �          d� Z	  ed�  �        Z e�   �           e	�   �          dZ  ee ez   �  �        Z!e!�"                    �   �         Z# ej$        e#�  �        Z% e�   �           e�   �           e�   �           e�   �          	 d� Z& e'd�  �          e&d�  �          e'd�  �          e j        d�  �         dS ) �    N)�urlopenc                  ��   � t          d�  �         t          d�  �         t          d�  �         t          d�  �         t          d�  �         t          d�  �         t          d�  �         d S )NzB[31m#############################################################z@[31m# [33m[1mIp Tracker		                         	    [31m#zF[31m# [33m[1mAccurate IP tracking Tool	                 	    [31m#zC[31m# [33m[1mAuthor: Are you ready soldiers 		            [31m#zP[31m# [33m[1mGitHub: https://github.com/cyberexit/Ip-Tracker           [31m#z8[31m# [33m[1mVersion: 1.0.1			            	    [31m#��print� �    �IpTracker.py�Bannar4r
      sq   � ��O�P�P�P��V�W�W�W��\�]�]�]��Y�Z�Z�Z��f�g�g�g��N�O�O�O��O�P�P�P�P�Pr   c                  �(  � t          dt          d         z   �  �         t          dt          d         z   �  �         t          dt          d         z   �  �         t          dt          d         z   �  �         t          d	t          d
         z   �  �         d S )Nz   [31m[1mQuery      : [33m�queryz   [31m[1mStatus     : [33m�statusz   [31m[1mCountry    : [33m�countryz   [31m[1mRegionName : [33m�
regionNamez   [31m[1mCity       : [33m�city�r   �valuesr   r   r	   �Ip1r      s�   � �	�4�v�g��F�G�G�G�	�4�v�h�7G�G�H�H�H�	�4�v�i�7H�H�I�I�I�	�4�v�l�7K�K�L�L�L�	�4�v�f�~�E�F�F�F�F�Fr   c                  �.   � t          j        d�  �         d S �N�5xdg-open https://facebook.com/groups/658498695902684/��os�systemr   r   r	   �Link1r      �   � ���B�C�C�C�C�Cr   c                  �.   � t          j        d�  �         d S r   r   r   r   r	   �Link2r      r   r   c                  �@   � t          d�  �         t          �   �          d S )Nz$Tap Enter Auto Track Your IP Addressr   r   r   r	   �Tapr      s   � ��.�/�/�/������r   c                  �(  � t          dt          d         z   �  �         t          dt          d         z   �  �         t          dt          d         z   �  �         t          dt          d         z   �  �         t          d	t          d
         z   �  �         d S )Nz   [31m[1mZipCode    : [33m�zipz   [31m[1mIsp        : [33m�isp�   [31m[1mOrg        : [33m�orgz   [31m[1mAs         : [33m�asz   [31m[1mRegion     : [33m�regionr   r   r   r	   �Ip2r'      s�   � �	�4�v�e�}�D�E�E�E�	�4�v�e�}�D�E�E�E�	�4�v�e�}�D�E�E�E�	�4�v�d�|�C�D�D�D�	�4�v�h�7G�G�H�H�H�H�Hr   c                  �L   � t          d�  �         t          j        d�  �         d S )Nz[36mzfiglet -f slant S O L D I E R�r   r   r   r   r   r	   �Bannar1r*   !   s'   � ��
������*�+�+�+�+�+r   c                  �L   � t          j        d�  �         t          d�  �         d S )Nzfiglet  IP T R A C K E Dz@[34m   {[31m[1m========================================[34m})r   r   r   r   r   r	   �Bannar2r,   $   s(   � ���%�&�&�&��V�W�W�W�W�Wr   c                  �h   � t          d�  �         t          j        d�  �         t          �   �          d S )Nz[33mzfiglet -f slant IP ADDRESSr)   r   r   r	   �Bannar3r.   '   s.   � ��
������'�(�(�(������r   c                  �.   � t          j        d�  �         d S )Nzfiglet -f slant T H A N K Sr   r   r   r	   �Thanksr0   +   s   � ���(�)�)�)�)�)r   c                  �.   � t          j        d�  �         d S )N�clearr   r   r   r	   �Clearr3   .   s   � ���7�����r   c                  �$   � t          d�  �         d S )Nz[33mwait....r   r   r   r	   �Withr5   0   s   � �������r   Tz


 [35m Enter username:z
Go to hellz


  [35mEnter password:�soldierg�������?z
[31m  Wrong password enteredg�Q���?r2   c                  �@   � t          dt          d         z   �  �         d S )Nr#   �geor   r   r   r	   �Ip3r9   J   s    � ��1�F�5�M�A�B�B�B�B�Br   z[31mTargeted ip:[32mzhttp://ip-api.com/json/c                 �   � | dz   D ]S}t           j        �                    |�  �         t           j        �                    �   �          t	          j        d�  �         �Td S )N�
g{�G�z�?)�sys�stdout�write�flush�time�sleep)�s�cs     r	   �	slowprintrD   Y   s\   � ���X� � ���
��������
�������
�8������ r   z8[95m+-------------------------------------------------+z�[95m|             Welcome To Hackers World            |
|             Joine Our Facebook Group            |
|             Are you ready soldiers              |
| Watch Ours Tutorials For Learn Ethical Hacking  |z3+-------------------------------------------------+r   )(r   �urllib.requestr   �jsonr@   r<   r
   r   r   r   r   r'   r*   r,   r.   r0   r3   r5   �input�a�b�x�zrA   �wr�ir=   r>   r?   r   r9   �ip�url�response�read�data�loadsr   rD   r   r   r   r	   �<module>rT      s#  �� 	�	�	�	� "� "� "� "� "� "� ���� ���� 
�
�
�
�Q� Q� Q�G� G� G�D� D� D�D� D� D�
� 
� 
�I� I� I�,� ,� ,�X� X� X�
� 
� 
�*� *� *�� � �� � � ����� ��
�
�
� ��
�
�
����/�0�0�A��A���/�0�0�A��A��A�v�v���
�3�����1��� 	� 	�A��J���Q�����J�������D�J�t�������	�'������
�
�
���
�
�
�!�" ����� ����� ��
�
�
� �����C� C� C�
��u�+�,�,�B��D�G�G�G�	�E�H�H�H�
#�C��w�s�R�x� � �H��=�=�?�?�D��T�Z����F�	�E�G�G�G��G�J�J�J��C�F�F�F��C�F�F�F�	�� � �
 ��C� D� D� D� 	�	� 7� 8� 8� 8� ��;� <� <� <� 	��	�
A� B� B� B� B� Br   