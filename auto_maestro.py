from subprocess import call, check_output
import os

def result_parse(result):
    each_ops = result.split("[Summary]")
    E = 0.0
    T = 0
    for ops in each_ops[1:]:
        E += float(ops.split(':')[2].split('X')[0]) # Total E
        T += int(ops.split(':')[4].split('cycles')[0]) # Total T

    return (E,T)

map_path = os.path.join(os.getcwd(),"data/mapping/vgg16_rs.m")
# hw_path = os.path.join(os.getcwd(),"data/hw/accelerator_1.m")

noc = 256
l1 = 256
l2 = 2048
num_pe = 256

result = check_output(["./maestro","--print_res=true",\
"--print_res_csv_file=false",\
"--print_log_file=false",\
"--Mapping_file={}".format(map_path),\
# "--HW_file={}".format(hw_path),\
"--noc_bw={}".format(noc),\
"--noc_hops=1",\
"--noc_hop_latency=1",\
"--l1_size={}".format(l1),\
"--l2_size={}".format(l2),\
"--num_pes={}".format(num_pe),\
"--print_design_space=true",\
"--msg_print_lv=0"],universal_newlines=True)

print(result_parse(result.replace('\n',':')))

# print()
# print(result_list[result_list.index('Total energy consumption')+1])
# print(result_list[result_list.index('Runtime')+1])
# print(result_list[result_list.index('Throughput')+1])
# print(result_list[result_list.index('Arithmetic intensity')+1])

