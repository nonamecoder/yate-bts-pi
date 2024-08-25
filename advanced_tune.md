## Fine Tuning

Yate's architecture is designed to generate as many future TX bursts as possible until the TX FIFOs start blocking. Essentially, `RadioInterface::send()` is supposed to block until there is enough buffer room between `libusb->FX3->FPGA` to fit another 1024 sample buffer.

Yate expects to generate a TX burst roughly 2 subframes before their RF transmission. To calculate how many samples 2 subframes correspond to, multiply the following:

- 2 subframes
- 8 timeslots / subframe
- 156.25 symbols / timeslot
- 8 IQ samples / symbol

\[
2 \times 8 \times 156.25 \times 8 = 20,000 \, \text{IQ samples}
\]

24 buffers × 1024 samples is about 24,576 samples, which (factoring in some processing lag) corresponds to Yate's expectation of sending TX bursts 2 subframes before RF transmission.

The buffer size, number of buffers, and number of transfers were chosen based on this methodology. However, they might need to be tuned depending on the USB host controller, CPU, and OS settings.

### How to Tune:

1. Define `#define BRF_DEBUG` at the top of `ybladerf.cpp` and recompile and install Yate.

2. Strong deviations from 20,000 samples are not good; however, issues typically arise (and become visible) if the time difference number drops below 5,000 (or goes negative). TX bursts will not make it to the FPGA in time to be sent over the SMA port. In this case, consider increasing the **number of buffers** and **number of transfers** in unison.

3. If CPU throughput is the issue, multiply `buffer_size` by a factor of 2, and divide **number of buffers** and **number of transfers** by the same number.

4. Increasing **number of transfers** is helpful if USB timeout errors appear. Care must be taken not to increase this number past 50% of the **number of buffers**.
