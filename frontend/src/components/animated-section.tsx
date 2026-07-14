"use client";

import { motion, useReducedMotion } from "framer-motion";
import { PropsWithChildren } from "react";

export function AnimatedSection({ children }: PropsWithChildren) {
  const reduced = useReducedMotion();

  return (
    <motion.section
      initial={reduced ? false : { opacity: 0, y: 20 }}
      whileInView={reduced ? {} : { opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.2 }}
      transition={{ duration: 0.5 }}
    >
      {children}
    </motion.section>
  );
}
