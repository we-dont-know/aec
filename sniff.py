
#sniff
import scapy.all as scapy

def sniff_packets(interface,filter=None):
    scapy.sniff(iface=interface,store=False,prn=process_packet,filter =None)

def process_packet(packet):
    if packet.haslayer(scapy.IP):
        ip_src=packet[scapy.IP].src
        ip_dst=packet[scapy.IP].dst
        protocol=packet[scapy.IP].proto
        if packet.haslayer(scapy.TCP):
            src_port=packet[scapy.TCP].sport
            dst_port=packet[scapy.TCP].dport
            print(f"ip packets:{src_port}-->{ip_dst}:{dst_port}")
        else:
            print(f"ip packets={ip_src}-->{ip_dst},protocol:{protocol}")

def main():
    interface=input("enter the interface to sniff on:")
    print("\n starting packet sniffing")
    sniff_packets(interface,filter)

if __name__ =='__main__':
    main()
